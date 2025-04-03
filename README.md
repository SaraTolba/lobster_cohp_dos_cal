# About LOBSTER COHP and DOS Calculation Toolkit

A comprehensive toolkit for calculating and analyzing Crystal Orbital Hamilton Population (COHP) and Density of States (DOS) using LOBSTER software with VASP output.

## Overview

This repository contains scripts for post-processing VASP and Lobster outputs to generate COHP, -ICOHP, and DOS data using LOBSTER software. These analyses help understand chemical bonding in materials and provide valuable insights into electronic structure.

## Workflow

### Preparation
1. Complete your geometry optimized (GO) VASP calculations
2. Copy CONTCAR to POSCAR
3. Edit the INCAR file:
   - Set `ISYM = -1`
   - Set `NSW = 0` (or `IBRION = -1`)
   - Add `NBANDS` parameter (extract this value from your GO job OUTCAR)
   - Set `LWAVE = .TRUE.`
4. Prepare the `lobsterin` file (see example below)

### Running LOBSTER
5. Execute LOBSTER in the same directory as your VASP files
6. Post-process the results using the scripts in this repository

## Example lobsterin File

```
COHPstartEnergy  -22
COHPendEnergy     18
basisSet  pbeVaspFit2015
gaussianSmearingWidth 0.1
includeOrbitals s p

cohpGenerator type S type O type H


basisFunctions C  2s 2p 
basisFunctions H  1s 
basisFunctions N  2s 2p
basisFunctions O  2s 2p
basisFunctions S  3s 3p


skipGrossPopulation
skipMadelungEnergy

```

## Scripts

This repository includes scripts for:
- Extracting and plotting COHP data
- Calculating integrated COHP values
- Generating DOS plots

## Dependencies

- Python 3.x
- pymatgen
- NumPy
- Matplotlib
- pandas
- [LOBSTER](http://www.cohp.de/) software

## Usage

Detailed examples and usage instructions are provided in the documentation folder.

## References

These scripts were developed following work by various researchers in the field:

- J. George, G. Petretto, A. Naik, M. Esters, A. J. Jackson, R. Nelson, R. Dronskowski, G.-M. Rignanese, G. Hautier, ChemPlusChem, 2022, e202200123.
- Some components were inspired by Janine George's notebook (janine.george@bam.de, BAM, https://jageo.github.io/)

## Learn More

For additional information about LOBSTER software and methodology, visit http://www.cohp.de

## Contributing

Contributions, bug reports, and feature requests are welcome! Please feel free to submit a pull request or open an issue.






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
