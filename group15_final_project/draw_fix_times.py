#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Description:
1. Purpose:
Get the high fix times in kernel v4.x version and draw the histogram, kernel density curve and varibable distribution diagram.

2. Result of function:
a) Function draw_hist will draw the high fix times after classifying in all sub versions.

3. Run method:
Run the command "python3 draw_fix_times.py" in shell.

"""

__author__ = "Group 15 in DataScience of Lanzhou University"
__copyright__ = "Copyright 2020, Group15 in DataScience of Lanzhou University , China"
__license__ = "GPL V3"
__version__ = "1.0"
__maintainer__ = "Yiqi Huang"
__email__ = ["huangyq2018@lzu.edu.cn"]
__status__ = "Done"

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
# staibility_test is a py file whose function classify will return the high fix times in one main version.
from staibility_test import *

def draw_hist(counter):
    sns.distplot(counter, color='orange', 
                 kde=True,          # Plot a kernel density curve
                 hist=True,         # Plot a histogram
                 rug=True,          # Plot a variable distribution diagram
                 kde_kws = {"shade": True, "color": 'darkorange','facecolor': 'gray'}, 
                 rug_kws = {'color': 'red','height': 0.1})

    plt.xlabel('Versions')
    plt.ylabel('Times')
    plt.title('Distribution of fix times with version_interval')
    plt.show()

# The following will be the version num with high fix times in one main version.
"""
v4_4 = [55, 63, 64, 68, 70, 74, 75, 82, 83, 88, 97, 99, 106, 110, 112, 114, 115, 116, 117, 120, 121, 122, 125, 127, 129, 136, 137, 142, 143, 146, 147, 151, 153, 155, 156, 161, 163, 164, 165, 166, 169, 173, 174, 175, 176, 177, 178, 179, 183, 188, 200, 201, 202, 205, 210, 214]
v4_9 = [55, 81, 86, 87, 88, 91, 92, 95, 102, 110, 114, 118, 119, 123, 126, 133, 134, 137, 140, 142, 157, 158, 159, 162, 164, 167, 171, 172, 173, 174, 178, 183, 185, 193, 199, 201, 202, 205, 209, 210, 211, 213, 214]
v4_14 = [19, 28, 34, 43, 52, 57, 62, 66, 68, 70, 74, 77, 79, 80, 81, 83, 84, 85, 87, 88, 96, 100, 103, 107, 110, 114, 115, 121, 122, 127, 128, 130, 133, 142, 144, 145, 152, 153, 154, 155, 156, 157, 158, 160, 162, 164, 166, 167, 170, 171]
v4_19 = [0, 39, 47, 59, 68, 71, 73, 74, 80, 83, 84, 85, 86, 87, 88, 89, 91, 95, 97, 99, 101, 102, 104, 106]

"""

if __name__ == "__main__":
    for i in classify(v):
        draw_hist(i)



