# plot COHPCAR.lobster

from pymatgen.electronic_structure.cohp import CompleteCohp
from pymatgen.electronic_structure.plotter import CohpPlotter

import matplotlib

from pymatgen.core.composition import Element
from pymatgen.electronic_structure.plotter import DosPlotter

# relevant classes
from pymatgen.io.lobster import Doscar


DOSCAR_path = "./DOSCAR.lobster"
POSCAR_path = "./POSCAR"

# read in DOSCAR.lobster
doscar = Doscar(
    doscar=DOSCAR_path, structure_file=POSCAR_path)
complete_dos = doscar.completedos
# get structure object
structure = complete_dos.structure


# plot total dos
cp = DosPlotter()
cp.add_dos("Total Dos", doscar.tdos)
# cp.get_plot().show()


# plot DOS of s,p, and d orbitals for certain element
# cp = DosPlotter()
# el = Element("H")
# cp.add_dos_dict(complete_dos.get_element_spd_dos(el=el))
# cp.get_plot().show()

x = cp.get_plot()
#x.ylim([-10, 6])
#x.show()

x.savefig("DOS.png",
            bbox_inches ="tight",
            transparent = True,
            dpi=1000,
            edgecolor ='w')


##--------- 
data=cp.get_dos_dict()
##define a file to save data in it:
sourceFile = open('DOS.json','w')
# Calulate and print averages for BindEnergys and volumes.
print(data, file = sourceFile)



