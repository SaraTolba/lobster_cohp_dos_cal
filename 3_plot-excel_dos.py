# Sara A. Tolba
#--------------------------------------plot PDOS------------------------------#
### python to plot excel sheets

import math
import pandas as pd
from numpy import round 
import os
from openpyxl.utils import get_column_letter
from openpyxl import load_workbook
from openpyxl.styles import Font
import sys

import matplotlib as mpl
from pylab import cm
import matplotlib.font_manager as fm

import matplotlib.pyplot as plt
import numpy as np
import csv
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
#--------------------------------------------------------------------------
import seaborn as sns


### ===================== Fig formatting ===================== ###

from matplotlib import rcParams, cycler
from matplotlib.ticker import AutoMinorLocator

# Using the 'seaborn-paper' style
# plt.style.use('seaborn-paper')
default_colors = sns.color_palette(palette='gnuplot2')	# or sns.color_palette() Dark2 Set2 tab10 gnuplot2
default_colors.as_hex()

print(default_colors.as_hex())

rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Arial']
rcParams['font.size'] = 14
rcParams['axes.linewidth'] = 1.1
rcParams['axes.labelpad'] = 10.0
rcParams['lines.linewidth'] = 1.5

plot_color_cycle = cycler('color', ['#2962FF', '#8d04fb', '#ff4eb1', '#ff9669', '#ffe01f'])
rcParams['axes.prop_cycle'] = plot_color_cycle
# rcParams['axes.xmargin'] = 0
rcParams['axes.ymargin'] = 0
rcParams.update({"figure.figsize" : (5,4.8),
                 "figure.subplot.left" : 0.177, "figure.subplot.right" : 0.946,
                 "figure.subplot.bottom" : 0.156, "figure.subplot.top" : 0.965,
                 "axes.autolimit_mode" : "round_numbers",
                 "xtick.major.size"     : 7,
                 "xtick.minor.size"     : 3.5,
                 "xtick.major.width"    : 1.1,
                 "xtick.minor.width"    : 1.1,
                 "xtick.major.pad"      : 5,
                 "xtick.minor.visible" : True,
                 "ytick.major.size"     : 7,
                 "ytick.minor.size"     : 3.5,
                 "ytick.major.width"    : 1.1,
                 "ytick.minor.width"    : 1.1,
                 "ytick.major.pad"      : 5,
                 "ytick.minor.visible" : True,
                 "lines.markersize" : 12,
#                  "lines.markerfacecolor" : "none",
                 "lines.markeredgewidth"  : 0.8})
                 
### ===================== Fig formatting ===================== ###

# Read data from a specific sheet in the Excel file
file_path = 'ZWs-dos.xlsx'  # Replace 'your_file.xlsx' with your actual file path
sheet_name = 'Sheet1'  # Replace 'Sheet1' with the name of your sheet
df1 = pd.read_excel(file_path, sheet_name=sheet_name)

# df2 = pd.read_excel(xlsx_file,header=0,sheet_name="polyMPC")
# df3 = pd.read_excel(xlsx_file,header=0,sheet_name="SB-6H2O")
# df4 = pd.read_excel(xlsx_file,header=0,sheet_name="MPC-2H2O")


E = df1.iloc[:,0] # list of the second column 
linPG = df1.iloc[:,1]
PE = df1.iloc[:,3]
PEG = df1.iloc[:,5]
PVP = df1.iloc[:,7]

# MPC_t = df2.iloc[:,1]


# Default colors used in matplotlib.pyplot
default_colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

# Plotting using Seaborn with default matplotlib colors
plt.figure()



# plt.plot(E, MPC_t,  color = (4/255,4/255,5/255) , label="Total" )	#1 black
# plt.fill_between(E, MPC_t, color=(4/255,4/255,5/255), alpha=0.15)

plt.plot(E, linPG,  color=default_colors[0], label="SB")		#2 purple
plt.fill_between(E, linPG, where=(E <= 0), color=default_colors[0], alpha=0.15)

plt.plot(E, PE,  color=default_colors[1], label="MPC")	#3 blue
plt.fill_between(E, PE, where=(E <= 0), color=default_colors[1], alpha=0.15)

plt.plot(E, PEG,  color=default_colors[2],label="CBAA")		#4 red
plt.fill_between(E, PEG, where=(E <= 0), color=default_colors[2], alpha=0.15)

plt.plot(E, PVP,  color=default_colors[3],label="SBi")		#5 orange
plt.fill_between(E, PVP, where=(E <= 0), color=default_colors[3], alpha=0.15)

# plt.plot(Temp, dGads_6H2O_mpc,  color = (139/255,138/255,140/255),label="9.69%",linewidth=1.8)



# Efermi line: only one line may be specified; full height
plt.axvline(x = 0, color = 'k', linestyle = ':', linewidth=1)




#plt.title('Count of O-H bond length in water')
plt.ylabel('Density of States')
plt.xlabel('Energy (eV)')
plt.legend(fontsize='small', loc='upper right')
# plt.legend(fontsize=18,fancybox=True,loc='best',framealpha=0,edgecolor='white',ncol=2) #upper left
# plt.tick_params(direction='in', length=6, width=2)
               
# plt.tick_params(which='major', length=5, width=2)
# plt.tick_params(which='minor', length=2.5, width=0.75)


plt.xlim(right=4.5)
plt.xlim(left=-3.5)  # or 12.1
plt.ylim(bottom=0)
plt.ylim(top=80)

plt.gca().xaxis.set_minor_locator(AutoMinorLocator(n=2))
plt.gca().yaxis.set_minor_locator(AutoMinorLocator(n=2))



plt.savefig("ZWpolys-DOS.png",
            bbox_inches ="tight",
            transparent = True,
            dpi=1000,
            edgecolor ='w')

plt.show()
