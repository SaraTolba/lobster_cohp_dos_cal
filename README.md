# lobster_cohp_dos_cal
Calculation Steps:
1- get your geometry optimized (GO) vasp calculations
2- copy CONTCAR to POSCAR
3- Edit the INCAR: change ISYM to -1, NSW to 0 (or IBRION=-1), insert NBANDS (get from GO job OUTCAR), and set LWAVE to True in the INCAR
4- Prepare the "lobsterin" file (see the example)
5-run Lobster
6- post processing

Scripts to post process vasp output to get the COHP, -ICOHP, and DOS using LOBSTER software
See http://www.cohp.de for more information 

Some parts of these scripts were written following a notebook by Janine George (E-mail: janine.george@bam.de BAM, https://jageo.github.io/).
Ref: J. George, G. Petretto, A. Naik, M. Esters, A. J. Jackson, R. Nelson, R. Dronskowski, G.-M. Rignanese, G. Hautier, ChemPlusChem n.d., n/a, e202200123.
