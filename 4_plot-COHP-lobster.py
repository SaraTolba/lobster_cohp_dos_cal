# plot COHPCAR.lobster

from pymatgen.electronic_structure.cohp import CompleteCohp
from pymatgen.electronic_structure.plotter import CohpPlotter

import matplotlib

COHPCAR_path = "./COHPCAR.lobster"
POSCAR_path = "./POSCAR"

completecohp = CompleteCohp.from_file(
    fmt="LOBSTER", filename=COHPCAR_path, structure_file=POSCAR_path
)


# search for the number of the COHP you would like to plot in ICOHPLIST.lobster (the numbers in COHPCAR.lobster are different!)
#     237         H168          O21  
#    104         H169           O8 
#   297         H168          O30   

label = "297"
cp = CohpPlotter(are_coops=False)
# get a nicer plot label
plotlabel = (
    str(completecohp.bonds[label]["sites"][0].species_string)
    + "-"
    + str(completecohp.bonds[label]["sites"][1].species_string)
)

cp.add_cohp(plotlabel, completecohp.get_cohp_by_label(label=label))
# check which COHP you are plotting

print(
    "This is a COHP between the following sites: "
    + str(completecohp.bonds[label]["sites"][0])
    + " and "
    + str(completecohp.bonds[label]["sites"][1])
)

x = cp.get_plot(xlim=None, ylim=None, plot_negative=None, integrated=False, invert_axes=False)
#x.ylim([-1, 1])

#x.show()

#x=cp.save_plot("namme", img_format='png', xlim=None, ylim=None)


# 

x.savefig("-cohp_wtO26-H90.png",
            bbox_inches ="tight",
            transparent = True,
            dpi=1000,
            edgecolor ='w')
            
##--------- 
data=cp.get_cohp_dict()
##define a file to save data in it:
sourceFile = open('cohp_wtO26-H90.json','w')
# Calulate and print averages for BindEnergys and volumes.
print(data, file = sourceFile)



# import pandas as pd
# 
# line = x.gca().get_lines()[0]
# data = pd.line.get_xydata()
# print(data)
# data=cp.get_cohp_dict()

# 

# sourceFile.close()

# df = pd.read_json (r'./results-text.json')
# df.to_csv(r'./results-text.csv', index = None)





