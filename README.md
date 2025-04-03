# LOBSTER COHP and DOS Calculation Toolkit

[![LOBSTER](https://img.shields.io/badge/LOBSTER-Chemical%20Bonding%20Analysis-blue)](http://www.cohp.de)
[![VASP](https://img.shields.io/badge/VASP-DFT%20Calculations-green)](https://www.vasp.at/)
[![Python](https://img.shields.io/badge/Python-3.x-yellow)](https://www.python.org/)

## 🔬 Analyze Chemical Bonding in Materials with LOBSTER and VASP

A comprehensive toolkit for calculating and analyzing **Crystal Orbital Hamilton Population (COHP)** and **Density of States (DOS)** using LOBSTER software with VASP output. Perfect for materials scientists, computational chemists, and researchers studying electronic structure and bonding properties.

![COHP Analysis Example](https://github.com/SaraTolba/lobster_cohp_dos_cal/blob/main/images/cohp_example.png)

## 📋 Features

- **COHP and Integrated COHP Analysis**: Extract and visualize chemical bonding information from VASP calculations
- **DOS Processing**: Generate and analyze density of states plots

## 🔧 Preparation Workflow

1. Complete your geometry optimized (GO) VASP calculations
2. Copy CONTCAR to POSCAR
3. Edit the INCAR file:
   - Set `ISYM = -1`
   - Set `NSW = 0` (or `IBRION = -1`)
   - Add `NBANDS` parameter (extract this value from your GO job OUTCAR)
   - Set `LWAVE = .TRUE.`
4. Prepare the `lobsterin` file (see example below)
5. Execute LOBSTER in the same directory as your VASP files
6. Post-process the results using the scripts in this repository

## 📝 Example lobsterin File

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

## 🧰 Scripts and Tools

This repository includes scripts for:
- **COHP Data Extraction**: Parse and organize LOBSTER output files
- **Bonding Analysis**: Identify and quantify bonding interactions in materials
- **Visualization**: Generate publication-quality plots for COHP and DOS data
- **Comparative Analysis**: Tools for comparing bonding properties across materials

## 📊 Example Results

![DOS Analysis Example](https://github.com/SaraTolba/lobster_cohp_dos_cal/blob/main/images/dos_example.png)

## 🔗 Dependencies

- Python 3.x
- pymatgen
- NumPy
- Matplotlib
- pandas
- [LOBSTER](http://www.cohp.de/) software


## 📖 Usage

More detailed examples and usage instructions are provided in the [documentation folder](https://github.com/SaraTolba/lobster_cohp_dos_cal/tree/main/docs).

## 🔍 Applications

- **Materials Science**: Analyze bonding in novel materials
- **Catalysis Research**: Understand surface-adsorbate interactions
- **Energy Materials**: Investigate the electronic properties of battery and photovoltaic materials
- **Computational Chemistry**: Supplement DFT calculations with bonding analysis

## 📚 References

These scripts were developed following work by various researchers in the field:

- J. George, G. Petretto, A. Naik, M. Esters, A. J. Jackson, R. Nelson, R. Dronskowski, G.-M. Rignanese, G. Hautier, ChemPlusChem, 2022, e202200123.
- Some components were inspired by Janine George's notebook (janine.george@bam.de, BAM, https://jageo.github.io/)
- LOBSTER software: [http://www.cohp.de](http://www.cohp.de)

## 👥 Contributing

Contributions, bug reports, and feature requests are welcome! Please feel free to:
- Submit a [pull request](https://github.com/SaraTolba/lobster_cohp_dos_cal/pulls)
- Open an [issue](https://github.com/SaraTolba/lobster_cohp_dos_cal/issues)


## 📧 Contact

For questions and support, please [open an issue](https://github.com/SaraTolba/lobster_cohp_dos_cal/issues)

## ⭐ Star this repository

If you find this toolkit helpful, please consider giving it a star on GitHub to help others discover it!

---

**Keywords**: LOBSTER, COHP, -ICOHP, DOS, VASP, DFT, computational materials science, chemical bonding, electronic structure, integrated COHP, density of states, materials simulation, quantum chemistry
