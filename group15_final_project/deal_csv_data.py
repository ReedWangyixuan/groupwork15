#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Description:

1. Purpose:
For the fix ampliture data in the csv file, I deal with it and calculate the mean value of the fix ampliture for each version.

2. Result of function:
a) Function "load_csv_data" return two list without title. One list stores add ampliture and another stores del ampliture.
b) Function "clean_diff" clean the data of the difference of add list and del list. After cleaning, the function return a list which stores the index of cleaned elements.
c) Function "calculate_ampliture" delet the element according to the index list and calculate the fix ampliture.
d) Function "calculate_mean" calculate the mean of the fix ampliture of different versions. 

3. Run method:
Run the command "python3 deal_csv_data.py" in shell.

"""

__author__ = "Group 15 in DataScience of Lanzhou University"
__copyright__ = "Copyright 2020, Group15 in DataScience of Lanzhou University , China"
__license__ = "GPL V3"
__version__ = "1.0"
__maintainer__ = "Yiqi Huang"
__email__ = ["huangyq2018@lzu.edu.cn"]
__status__ = "Done"

import csv, string
import numpy as np

def load_csv_data(i):
    """
    Load the add data and del data from csv file. Transform data from str to int.
    Return two list after cleaning which is add and dele.
    Argument: i is the cloumn number, which is also the order number of version.

    """
    def filter_function(n):
        """
        Define the function for filtering. It will filter the empty string in the list.

        """
        n = n.translate(str.maketrans('', '', string.punctuation))
        return n and n.strip()
    
    with open("fix_ampliture(clean).csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        add = [row[3*i] for row in reader]
        add = list(filter(filter_function, add)) # filter the empty string in list.
        add = list(map(int, add[1:])) # tranform data type from str to int.

    with open("fix_ampliture(clean).csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        dele = [row[1+3*i] for row in reader]
        dele = list(filter(filter_function, dele))
        dele = list(map(int, dele[1:]))
        
        return add, dele

def clean_diff():
    """
    Clean some data which is not suitable for the hypothesis like the fix for refactoring.
    Return the index of deleted elements in origin list. 
    
    """
    diff_idx_res = []
    for i in range(0,21):
        add,dele = load_csv_data(i)
        """
        If add and dele subtract less than 3, that is, 
        the amount of code deleted and added is similar,
        I can think of the commit as a refactoring,
        not an addition of features or functionality.
        
        """
        diff_original = [abs(add_item - dele_item) for add_item, dele_item in zip(add,dele)]
        diff_clean = list(filter(lambda x:x > 3, diff_original)) #filter the element.
        diff = [i for i in diff_original if i not in diff_clean]
	# get the index list of the refactor element in each version.
        idx = [i for i,x in enumerate(diff_original) if x in diff]
        diff_idx_res.append(idx)
    return diff_idx_res

def calculate_ampliture(diff_idx_res):
    """
    For the index list returned by function clean_diff, I will delete the data in origin data list according to the index list.
    Return the mean of the list which stores fix ampliture.
    
    """
    ampliture_res = []
    for i in range(0,21):
        add,dele = load_csv_data(i)
        for j in diff_idx_res[i]:
            """
            Clean the data in the add_list and dele_list
            Del cannot be used because Del causes add and DeLe to get smaller and smaller.Because del is constantly deleted from the original list.
            Instead, let the dirty data replace by None type.
            """
            add[j] = ""
            dele[j] = ""
        add = list(filter(None,add))
        dele = list(filter(None,dele))
        ampliture = [add_item + dele_item for add_item, dele_item in zip(add,dele)]
        ampliture_res.append(ampliture)
    return ampliture_res

def calculate_mean(ampliture_res):
    """
    For the cleaned data, we can calculate the mean of the fix_ampliture.
    Return the mean of fix_ampliture list.
    
    """
    ampliture_mean = []
    for item in ampliture_res:
        mean = np.mean(item)
        ampliture_mean.append(mean)
    return ampliture_mean

def get_mean():
    """
    The main function.
    
    """
    diff_idx_res = clean_diff()
    ampliture_res = calculate_ampliture(diff_idx_res)
    ampliture_mean = calculate_mean(ampliture_res)
    return ampliture_mean

"""
if __name__ == "__main__":
    ampliture_mean = get_mean()
    print(ampliture_mean)
"""














