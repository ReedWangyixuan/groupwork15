#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Description:
1. Purpose:
Encapsulate git command "git log --pretty=format: "%ad" -1 [commit_id]" and "git log -p --no-merges [kernelRange]".
Get the commit_date from git kernel and write the data into the csv file.

2. Result of method:
a) getFixCommit returns a list stores the commit number of different versions.
b) getFixDate returns the fix_time list in order.
c) get_time_interval returns the time_interval list.

3. Run method:
Run the command "python3 getTimeInterval.py" in shell.
In other python file, import getTimeInterval, you can get the time_interval_list with method getTimeInterval.fixtime_list.

"""

__author__ = "Group 15 in DataScience of Lanzhou University"
__copyright__ = "Copyright 2020, Group15 in DataScience of Lanzhou University , China"
__license__ = "GPL V3"
__version__ = "1.0"
__maintainer__ = "Yiqi Huang"
__email__ = ["huangyq2018@lzu.edu.cn"]
__status__ = "Done"

from subprocess import Popen, PIPE
import re,time,unicodedata
import pandas as pd

class FixTimeInterval():
    def __init__(self, kernelRange, repo):
        self.kernelRange = kernelRange
        self.repo = repo

    def getFixCommits(self):
        """
        Get the commit number of fixes from the kernel with the git command.
        Return a list stores the commit number of different versions.

        """
        # use regular expression to match the content.
        commit = re.compile('^commit [0-9a-z]{40}$', re.IGNORECASE)
        fixes = re.compile('^\W+Fixes: [a-f0-9]{8,40} \(.*\)$', re.IGNORECASE)
        nr_fixes = 0
        fix_commit = []
        cmd = ["git", "log", "-p", "--no-merges", self.kernelRange]
        p = Popen(cmd, cwd=self.repo, stdout=PIPE)
        data, res = p.communicate()
        data = unicodedata.normalize(u'NFKD', data.decode(encoding="utf-8", errors="ignore"))
        for line in data.split("\n"):
            if(commit.match(line)): # match the commit
                cur_commit = line
            if(fixes.match(line)): # match the fixes
                nr_fixes += 1
                fix_commit.append(cur_commit[7:19])
        #print("total found fixes:",nr_fixes)
        return fix_commit

    def getFixDate(self):
        """
        Get the fix commit date and order them.
        Return the fix_time list in order.
        Arguments: fix_commit is a list stores the fix_commit number.

        """
        sort_date_stamp = []
        for commit_id in self.getFixCommits():
            cmd = ["git","log","--pretty=format:\"%ad\"","-1", commit_id]
            p = Popen(cmd, cwd=self.repo, stdout=PIPE)
            date, res = p.communicate()
            date = unicodedata.normalize(u'NFKD', date.decode(encoding="utf-8", errors="ignore"))
            dateStamp = time.mktime(time.strptime(date[:-7].strip('"'),"%a %b %d %H:%M:%S %Y")) # trun the date into timestamp
            sort_date_stamp.append(dateStamp)
        sort_date_stamp.sort()
        return sort_date_stamp

    def get_time_interval(self):
        """
        The difference of two functions and this difference is the intervl of time.
        Return the time_interval list.
        Arguments: sort_data_stamp is a sorted list stores the commit time.

        """
        time_interval0 = self.getFixDate()[:-1] # get the list without last element.
        time_interval1 = self.getFixDate()[1:] # get the list without first element.
        time_interval = [y-x for x,y in zip(time_interval0, time_interval1)] # Use two list to get the difference of fix_time.
        return time_interval

    def data_to_csv(self):
        """
        Load the data into a csv file.
        Return the status if the data is wrote into file successfully.
        Arguments: time_interval is the list stores the difference of the fix_time.

        """
        res_list = []
        for interval in self.get_time_interval():
            res_list.append([interval])
        title = [self.kernelRange]
        res = pd.DataFrame(columns=title, data=res_list) # transform into the dataframe type.
        res.to_csv(r"./Fixtime_Interval.csv")
        print("Succeed importing.")


if __name__ == "__main__":
    repo = "/Users/apple/linux-stable"
    kernelRange = "v4.0...v4.0.9"
    FTI = FixTimeInterval(kernelRange,repo)
    time_interval = FTI.get_time_interval()
    print(time_interval)
    #FTI.data_to_csv()


