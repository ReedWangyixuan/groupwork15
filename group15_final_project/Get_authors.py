#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
This py can find authors' number of each version.
'''

__author__ = "Group 15 members in DataScience of Lanzhou University"
__copyright__ = "Copyright 2020, Group15 in DataScience of Lanzhou University , China"
__license__ = "GPL V3"
__version__ = "1.0"
__maintainer__ = "Chunyao Dong"
__email__ = ["dongchy18@lzu.edu.cn"]
__status__ = "Done"


import re, subprocess


def GetAuthors(scope,address):
    '''
    This function can return authors' number of each version of provided range.
    The scope should be like ('v4.4.1','v4.4.100') or ('v4.4','v4.9'), attention the big version should be the same, ('v3.4','v4.6') cannot run.
    The address should be the location of the git in self computer.
    '''
    scope_begin = int(scope[0].split(".")[-1])
    scope_end = int(scope[1].split(".")[-1])
    momversion = scope[0].strip(str(scope_begin))
    auts = []
    for i in range(scope_begin,scope_end+1):
        rev1 = momversion + str(i)
        rev2 = momversion + str(i+1)
        gitcnt = "git rev-list --pretty=format:\"%an\" " + rev1 + "..." + rev2
        git_rev_list = subprocess.Popen(gitcnt, cwd=address, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, shell=True)
        raw_counts = git_rev_list.communicate()[0]
        cnt = re.findall('n[A-Z][a-z]* ', str(raw_counts))
        aut = []
        for j in cnt:
            if j not in aut:
                aut.append(j)
        auts.append(len(aut))
    return auts


if __name__ == "__main__":
    address = "/Users/apple/linux-stable"
    scope = ("v4.0","v4.19")
    print(GetAuthors(scope,address))#[951, 948, 994, 956, 951, 1030, 946, 973, 1005, 1010, 1014, 1085, 1039, 1082, 1108, 1096, 1055, 1066, 1086, 1094]
