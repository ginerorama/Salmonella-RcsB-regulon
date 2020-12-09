#!/usr/bin/env python3

##
## find_motif.py
## Script to find and annotates RcsB DNA binding motifs in Salmonella enterica subsp. enterica serovar Typhimurium SL1344 genome
## 
## Joaquin Giner Lamia 2020


# Modules
import re
from Bio import SeqIO,Seq



## Genome in GBK file
Salmonella_gbk_file = open("SL1344.gbk","r") 


## Parameters
DNA_motif=  "T.[GA]GA[ATGC]{4}TCC.A" 
windows_size = 500



## Functions

def get_RcsB_sites(Salmonella_gbk_file, DNA_motif):
	
	""" 
	This function retrieve RcsB motif sites in the 
	Salmonella genome sequence of the genbank file
	using Regex expression stored at DNA_motif variable.

	"""


	RcsB_sites = []
	motif = ""

	records = SeqIO.parse(Salmonella_gbk_file,"genbank")
	for record in records:
		sequence = record.seq

		result = re.finditer(DNA_motif,str(sequence)) #T.[GATC]GA[ATGC]{5}CT.A ..[GA]GA[ATGC]{4}[TC]CT.. T..GA[ATGC]{4}.CT..|...GA[ATGC]{4}.CT.A ...GA[ATGC]{4}.CT...
	
		for res in result:
			motif = res.group()	

			pos = str(res.start())

			site = motif+"@"+pos
			RcsB_sites.append(site)

				
			
	return RcsB_sites



def get_distance_to_TSS(strand,RcsB_site,locus):	

	"""
	obtain distance to TSS position for each locus that contains
	a RcsB motif site, in case that locus has a mapped TSS position.
	Salmonella TSS positions were retrieved from:
	http://bioinf.gen.tcd.ie/cgi-bin/salcom.pl?_HL 

	"""

	
	distance_list = []
	distance = "NA"	
	Salmonella_TSS_file = open("Salmonella_TSS.tsv","r")
	for line in Salmonella_TSS_file:
		orf = line.split("\t")[2]
		TSS_position = line.split("\t")[0]
		

		if orf == locus:
			if strand == -1:
				distance = int(TSS_position) - int(RcsB_site)	

			if strand == +1:
				distance = int(RcsB_site) - int(TSS_position) 

			distance_list.append(distance)	
	


	return distance_list	





def annotate_RcsB_sites(RcsB_sites,windows_size):

	""" 
	This function retrieve gene annotations for each 
	RcsB motif site either intergenic or intragenic.

	Header of result table:

	RcsB_genomic_position
	strand of genomic feature associated with the RcsB motif site
	RcsB motif site region (intragenic or itergenic)
	Relative position of motif site respect to ATG codon
	List of relative positions for each motif respect to TSS or TSSs (in case the locus has more than one TSS) 
	Sequence of RcsB motif site
	Locus
	motif start
	motif end
	gene common name
	description

	"""



	Salmonella_gbk_file = open("SL1344.gbk","r")
	records = SeqIO.parse(Salmonella_gbk_file,"genbank")
	for record in records:
		
		name = record.id

		for feature in record.features:
			for feature_class in  ["CDS","gene","ncRNA"]:
				if feature.type == feature_class:
					start = feature.location.start
					end = feature.location.end
					strand =  feature.location.strand
					try:
						product = feature.qualifiers['product'][0]
					except:
						product ="NA"

					try:		
						gene = feature.qualifiers['gene'][0]
					except:
						gene = "NA"	

					try:
						locus = feature.qualifiers['old_locus_tag'][0].replace("SL1344_","SL")
					except:
						locus = "NA"	




					if feature_class == "CDS":	
						if strand > 0:
							for site in RcsB_sites:
								site = site.split("@")
								motif = site[0]
								pos = int(site[1])
								relative_pos_atg = pos -start
								


								if int(start)-windows_size < pos < int(start):
									distance_to_TSS = get_distance_to_TSS(strand,pos,locus)

									print(str(pos)+"\t"+"+"+"\t"+"promoter"+"\t"+str(relative_pos_atg)+"\t"+str(distance_to_TSS)+"\t"+motif+"\t"+locus+"\t"+str(start)+"\t"+str(end)+"\t"+gene+"\t"+product)


								if int(start) < pos < int(end):	
									relative_pos_atg = -1*relative_pos_atg
									distance_to_TSS = get_distance_to_TSS(strand,pos,locus)
									line = str(pos)+"\t"+"+"+"\t"+"intragenic"+"\t"+str(relative_pos_atg)+"\t"+str(distance_to_TSS)+"\t"+motif+"\t"+locus+"\t"+str(start)+"\t"+str(end)+"\t"+gene+"\t"+product
									print(line)

						if strand < 0:

								
							for site in RcsB_sites:
								site = site.split("@")
								motif = site[0]
								pos = int(site[1])
								relative_pos_atg = end - pos	
								distance_to_TSS = get_distance_to_TSS(strand,pos,locus)


								if int(end) < pos < int(end)+windows_size:
									distance_to_TSS = get_distance_to_TSS(strand,pos,locus)

									print(str(pos)+"\t"+"-"+"\t"+"promoter"+"\t"+str(relative_pos_atg)+"\t"+str(distance_to_TSS)+"\t"+motif+"\t"+locus+"\t"+str(start)+"\t"+str(end)+"\t"+gene+"\t"+product)
								
								if int(start) < pos < int(end):	
									relative_pos_atg = -1*relative_pos_atg
									distance_to_TSS = get_distance_to_TSS(strand,pos,locus)

									line = str(pos)+"\t"+"-"+"\t"+"intragenic"+"\t"+str(relative_pos_atg)+"\t"+str(distance_to_TSS)+"\t"+motif+"\t"+locus+"\t"+str(start)+"\t"+str(end)+"\t"+gene+"\t"+product
									print(line)







def main(Salmonella_gbk_file,DNA_motif,windows_size):
	
	RcsB_sites = get_RcsB_sites(Salmonella_gbk_file,DNA_motif)
	annotate_RcsB_sites(RcsB_sites,windows_size)


if __name__ == "__main__":
	main(Salmonella_gbk_file,DNA_motif,windows_size)





