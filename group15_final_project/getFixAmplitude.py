#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Description:

1. Purpose:
Encapsulate git command "git diff --numstat v4.x..v4.x+1". Get the data from git kernel and write the data into the csv file.

2. Result of function:
a) Return  embedded list whose element is a list stores the nuber of adding lines, the number of deleting lines and the file path.
b) Write the data to the csv file and print the succeed importing status.

3. Run method:
Run the command "python3 getFixAmplitude.py" in shell.

"""

__author__ = "Group 15 members in DataScience of Lanzhou University"
__copyright__ = "Copyright 2020, Group15 in DataScience of Lanzhou University , China"
__license__ = "GPL V3"
__version__ = "1.0"
__maintainer__ = "Yiqi Huang"
__email__ = ["huangyq2018@lzu.edu.cn"]
__status__ = "Done"

from subprocess import Popen, PIPE
import unicodedata
import pandas as pd

class FixAmplitude():
    def __init__(self, kernelRange, repo):
        self.kernelRange = kernelRange
        self.repo = repo  

    def getFixAmplitude(self):
        """
        Get the nubmber of add lines and delete lines, which comes from the kernel in the shell.
        Return  embedded list whose element is a list stores the nuber of adding lines, the number of deleting lines and the file path.
        Arguments: kernelRange is the version number; repo is the path of commands work. 
    
        """
        cmd = ["git", "diff", "--numstat", self.kernelRange]
        p = Popen(cmd, cwd=self.repo, stdout=PIPE)
        data, res = p.communicate()
        data = unicodedata.normalize(u'NFKD', data.decode(encoding="utf-8", errors="ignore"))
        # remove the "\n" and "\t" in the data.
        data_split_line_break = data.split("\n")
        res = []
        for item in data_split_line_break:
            data_split_tab = item.split("\t")
            res.append(data_split_tab)
        return res[:-1]

    def data_to_csv(self, res, i):
        """
        Write the data into the csv file, after import, it will print a reminder "Succeed Loading. (with the number of version)"
        Arguments: res is a list; i is the number of the version.
    
        """
        title = ["add", "del", "file_path"]
        res = pd.DataFrame(columns=title, data=res)
        res.to_csv(r"./Fixtime_Interval_v4.%d.csv" % i)
        print("Succeed importing. v4.%d" % i)


if __name__ == "__main__":
    repo = "/Users/apple/linux-stable"
    for i in range(0,20):
        kernelRange = "v4.%d...v4.%d" % (i,(i+1))
        amp = FixAmplitude(kernelRange,repo)
        res = amp.getFixAmplitude()
        #amp.data_to_csv(res, i)



