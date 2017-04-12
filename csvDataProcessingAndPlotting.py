#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 20:53:40 2017
@author: ziaul_choudhury
"""

import csv
import matplotlib.pyplot as plt
import numpy as np 

def showData():
    csv_file = open('NYPD_Motor_Vehicle_Collisions_10468.csv')  #opening csv file in python
    csv_reader = csv.reader(csv_file, delimiter=',')        #providing delimiter to read value after specific symbol
    
    d = []     #lists the will store the values
    h = []
    k = []
    
    for row in csv_reader:              #reading row 0,1 for date and time
        date = row[0]
        print(date) 
        monthNum =(date[:2])
        d.append(monthNum)                  #Storing those values as list
        
    d.remove('DA')                    #removing unwanted DA value
    
    print ('\nDate only\n\n', d)#printing the list to make sure that I get the right value
    
    for s in d:                         #changing : to . so I can treat the list as to find unique number
        h.append(s)   
    h.sort()                            #sorting the list
 
    b = np.unique(h).tolist()           #Finding the unique values which is in time by using numpy
    print('Unique Values for hours: ', b)
    
    from itertools import groupby       #Unsing iterator tools to find occrences of collisons each hour
    k = ([len(list(group)) for key, group in groupby(h)])
    print('Unique Values for collisons: ', k)
    
    # Scatter Plot
    plt.plot(b, k, color='r', label="collisions")     #Plot collisions as red
    plt.title("Total number of collisions occared in every month")       #Title for plot
    plt.xlabel('Months 1 - 12')                     #Label for x-axis
    plt.ylabel('Occorences')                   #Label for the y-axis
    plt.legend(loc = 2,fontsize = 'x-small')#Make a legend in upper left corner
    plt.show()

        
showData()
