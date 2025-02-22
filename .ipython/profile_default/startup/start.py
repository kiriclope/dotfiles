from IPython import get_ipython
ipython = get_ipython()

try:
    from IPython.core import ultratb
    ultratb.VerboseTB._tb_highlight = "bg:ansired"
except Exception:
    print("Error patching background color for tracebacks, they'll be the ugly default instead")
    
# If in ipython, load autoreload extension
if 'ipython' in globals():
    print('\nWelcome to IPython!')
    ipython.run_line_magic('load_ext', 'autoreload')
    ipython.run_line_magic('autoreload', '2')

# Display all cell outputs in notebook
# from IPython.core.interactiveshell import InteractiveShell
# InteractiveShell.ast_node_interactivity = 'all'

import numpy as np
import matplotlib.pyplot as plt
from seaborn import set_context, set_style

# Pandas options
# pd.options.display.max_columns = 5
# pd.options.display.max_rows = 5

print('Your favorite libraries have been loaded.')

# plt.style.use('ggplot')

golden_ratio = (5**.5 - 1) / 2
width = 8
fig_size =  [width, width * golden_ratio]

plt.rcParams['figure.figsize'] = fig_size
plt.rcParams['figure.autolayout'] = True

plt.rcParams['lines.linewidth'] = 1
plt.rcParams['lines.markeredgewidth'] = 1
plt.rcParams['lines.markersize'] = 6
plt.rcParams['font.size'] = 12
plt.rcParams['legend.fontsize'] = 10
plt.rcParams['axes.facecolor'] = '1'
plt.rcParams['axes.edgecolor'] = '0'
plt.rcParams['axes.linewidth'] = '1'

plt.rcParams['axes.labelcolor'] = '0'
plt.rcParams['axes.labelsize'] = 10
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10
plt.rcParams['xtick.color'] = '0'
plt.rcParams['ytick.color'] = '0'
plt.rcParams['xtick.major.size'] = 2
plt.rcParams['ytick.major.size'] = 2

plt.rcParams['font.sans-serif'] = 'Arial'
plt.ion()

set_context("poster")
set_style("ticks")
plt.rc("axes.spines", top=False, right=False)
