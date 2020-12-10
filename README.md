# Salmonella RcsB Regulon Finder

This repository provides access to the script used to scan RcsB motif sites in *Salmonella enterica subsp. enterica serovar Typhimurium* SL1344 genome 
presented in the article:

### Structure-based analyses of Salmonella RcsB variants unravel new features of the Rcs regulon

Juanjo Huesa<sup>1</sup>,<sup>2</sup>†, Joaquín Giner-Lamia<sup>3,4†</sup> M. Graciela Pucciarelli<sup>3,5</sup>, Francisco Paredes-Martínez<sup>1,2</sup>  
Francisco García-del Portillo<sup>3*</sup>, Alberto Marina<sup>6,7*</sup> and Patricia Casino<sup>1,2,7*</sup>

<sup><sup>1</sup>Departamento de Bioquímica y Biología Molecular, Universitat de València. Dr Moliner 50, 46100 Burjassot, Spain; 
<sup>2</sup>Estructura de Recerca Interdisciplinar en Biotecnologia i Biomedicina (ERI BIOTECMED), Universitat de València. Dr Moliner 50, 46100 Burjassot, Spain. 
<sup>3</sup>Laboratorio de Patógenos Bacterianos Intracelulares. Centro Nacional de Biotecnología (CNB)-CSIC. Darwin, 3. 28049 Madrid. Spain.
<sup>4</sup>Centro de Biotecnología y Genómica de Plantas (CBGP, UPM-INIA), Universidad Politécnica de Madrid (UPM), Campus Montegancedo-UPM, E-28223 Pozuelo de Alarcón, Madrid, Spain
<sup>5</sup>Centro de Biología Molecular ’Severo Ochoa’ (CBMSO)-CSIC. Departamento de Biología Molecular. Universidad Autónoma de Madrid, Madrid, Spain.
<sup>6</sup>Department of Genomic and Proteomic, Instituto de Biomedicina de Valencia (IBV-CSIC), Jaume Roig 11, 46010 Valencia, Spain; 
<sup>7</sup>Group 739 of the Centro de Investigación Biomédica en Red sobre Enfermedades Raras (CIBERER) del Instituto de Salud Carlos III, Spain.</sup>

<sup>†These authors contributed equally to the paper as first authors.</sup>


<br>
<br>

## genome_scan.py

#### A Python script to find and annotate RcsB DNA binding motifs in *Salmonella enterica subsp. enterica serovar Typhimurium SL1344 genome* 

Joaquin Giner Lamia 2020

**usage:**

`python genome_scan.py`

**Required modules:**

Biopython



**Required files:**

*SL1344.gbk*   

​	Salmonella enterica subsp. enterica serovar Typhimurium SL1344 genbank file

​	Accession: NC_016810

​	Assembly: GCF_000210855.2

*Salmonella_TSS.tsv*

​	Retrieved from http://bioinf.gen.tcd.ie/cgi-bin/salcom.pl?_HL



**output format:**

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
