# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 18:43:56 2023

@author: KIIT
"""
import math

def nearest_negibour_algo(cities):
    n=len(cities)
    visited=[False]*n
    path=[0]*n
    path[0]=start=0
    visited[start]=True
    for i in range(1,n):
        min_dist=math.inf
        for j in range(n):
            if not visited[j]:
                dist=distance(cities[start],cities[j])
                if dist<min_dist:
                    min_dist=dist
                    next_city=j
        visited[next_city]=True
        path[i]=next_city
        start=next_city
    return path


def distance(city1,city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1]-city2[1])**2)


if __name__=="__main__":
    #cities=[(0,0),(1,2),(3,1),(2,3)]
    #cities=[(0,10),(15,20),(5,0),(9,10),(6,13),(0,12),(8,8),(9,0)]
    cities=[(0,10,15,20),(5,0,9,10),(6,13,0,12),(8,8,9,0)]
    path=nearest_negibour_algo(cities)
    print(path)
    
 
                