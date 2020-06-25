#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
This py contains a class which can use K-means algorithm to classify some data.
'''

__author__ = "Group 15 members in DataScience of Lanzhou University"
__copyright__ = "Copyright 2020, Group15 in DataScience of Lanzhou University , China"
__license__ = "GPL V3"
__version__ = "1.0"
__maintainer__ = "Chunyao Dong"
__email__ = ["dongchy18@lzu.edu.cn"]
__status__ = "Done"


from matplotlib import pyplot as plt
import numpy as np
import random
import sys

class KMeansClusterer():
    def __init__(self, array, cluster_num):
        '''
        array: the data's gather list. array should be like: [[1,2],[2,3],[10,9]]
        cluster_num: how many clusters you want the data to be classified.
        '''
        self.array = array
        self.ndarray = np.array(array)
        self.cluster_num = cluster_num
        self.points = self.__pick_start_point(self.ndarray, cluster_num)

    def cluster(self):
        '''
        return: the classified data array.
        '''
        result = []
        for i in range(self.cluster_num):
            result.append([])
        for item in self.ndarray:
            distance_min = sys.maxsize
            index = -1
            for i in range(len(self.points)):
                distance = self.__distance(item, self.points[i])
                if distance < distance_min:
                    distance_min = distance
                    index = i
            result[index] = result[index] + [item.tolist()]
        new_center = []
        for item in result:
            new_center.append(self.__center(item).tolist())
        if (self.points == new_center).all():
            return result
        self.points = np.array(new_center)
        return self.cluster()

    def __center(self, list):
        '''
        Compute the center of a set of coordinates
        '''
        return np.array(list).mean(axis=0)

    def __distance(self, p1, p2):
        '''
        Calculate the distance between two points
        '''
        tmp = 0
        for i in range(len(p1)):
            tmp += pow(p1[i] - p2[i], 2)
        return pow(tmp, 0.5)

    def __pick_start_point(self, ndarray, cluster_num):
        '''
        Pick the start point.
        '''
        if cluster_num < 0 or cluster_num > ndarray.shape[0]:
            raise Exception("cluster number is wrong.")
        indexes = random.sample(np.arange(0, ndarray.shape[0], step=1).tolist(), cluster_num)
        points = []
        for index in indexes:
            points.append(ndarray[index].tolist())
        return np.array(points)

    def location(self):
        '''
        Find the location of the each cluster.
        return: the subscripts of each data in the initail list.
        '''
        location = []
        for i in self.cluster():
            num = []
            for j in i:
                for k in range(len(self.array)):
                    if self.array[k] == j:
                        num.append(k)
            location.append(num)
        return location

    def show_2d(self):
        '''
        Only  the cluster number is 2 the plot can be showed.
        '''
        for i in self.cluster():
            colorArr = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
            color = ""
            for k in range(6):
                color += colorArr[random.randint(0, 14)]
            for j in i:
                plt.scatter(j[0], j[1], c= "#" + color)
        plt.title("K-means clustering")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.show()




