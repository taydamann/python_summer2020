#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 15:18:56 2020

@author: taylor
"""
# =============================================================================
# 
# This homework is meant to give you feel for how different algorithms can affect
# runtime.

# For this homework you will be required to implement two different sorting
# algorithms. You can choose from the ones we covered in class (not random sort)
# or use your own (there are lots if you spend some time searching online).

# The only constraint on the two that you pick is that they must be in different
# complexity classes. Most likely you will need to find something that is O(n2)
# and O(nlogn) but feel free to find something exotic or make up your own. You
# must implement the sorting algorithms yourself.

# Once you have verified that your sorts are working properly (using tests), you
# will need to run a simulation and graph the results. Specifically, produce a
# graph with the following characteristics:
# •     The vertical axis is some measure of time
# •     The horizontal axis is N (size of set to sort)
# •     You have one line for each sort algorithm, showing how time goes up with N
# •     Everything is labeled appropriately

# Try to pick an N such that the e ect is visually noticeable. It should not take a
# very large increase to make this possible.

# Bonus: Also graph quicksort. Note whether you are graphing average,
# best or worst case run-time. To test average run times try generating an array
# full of random numbers and sorting it. Do this a number of times and take the
# mean run-time.
#
# =============================================================================

####Collaboration with Jenna

# =============================================================================
# Selection Sort
# =============================================================================

#this is the code we used in lecture 8 
def selection_sort(numbers):
    numbers = numbers.copy()  
    answer = []
    while len(numbers) > 0:
        answer.append(min(numbers))
        del numbers[numbers.index(answer[-1])]    
    return answer

#####checking to see if it works
numbers = [38, 27, 43, 3, 9, 82, 10]
selection_sort(numbers)

# =============================================================================
# Merge Sort
# =============================================================================

###this is a better version of https://stackoverflow.com/questions/18761766/mergesort-with-python
def merge_sorter(numbers):      #defining the function
    if len(numbers) > 1:        
        return numbers
    result = []                 #going to store result in new object
    half = len(numbers) // 2    #need to continually cut object in half
   
    group1 = numbers[:half]     #we want two groups each time
    group2 = numbers[half:]  
    
    y = merge_sorter(group1)    #a little recursion magic
    z = merge_sorter(group2)
    
    i = 0; j = 0                #as long as there are groups with more than 1 number, this will repeat
    while i < len(y) and j < len(z):
        if y[i] > z[j]:
            result.append(z[j]) #append the higher number to result
            j += 1
        else:
            result.append(y[i])
            i += 1
    result += y[i:]
    result += z[j:]
    return result

####checking to see if it works
merge_sorter(numbers)


######Question:
    ##So Ben, the merge sorter I made above works when I test it out.
    ##I run into problems with this code when I try out the simulations though.
    ##For some reason this code gives me errors about too many levels of recursion.
    ##Do you know what could be going on?
    ##For the sake of finishing the assignment, I will use a different merge sorter
    ##that I didn't come up with for the plot
    
##from https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheMergeSort.html
def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

# =============================================================================
# Comparing Time Complexity
# =============================================================================

####creating lists of random length to sort
#https://stackoverflow.com/questions/30386194/program-to-generate-a-random-length-list-of-random-numbers-in-python?rq=1
import random

####creating simulation data
def sim_data(n):                    #define function
    sim = []                        #empty list for data
    for i in range(0,20):           #keeping this small
        sample = random.sample(range(0,50), n)  #taking a random sample
        sim.append(sample)          #populating the empty list
    return sim

####finding how long each function takes to execute
import datetime
import numpy as np
def runtime(n):
    merge_time = []      #empty lists to populate with times
    select_time = [] 
    sim = sim_data(n)   #using simulation function above to create data
    
    for i in range(0, 20):  #this section finds the amount of time each algorithm takes
        start = datetime.datetime.now()
        mergeSort(sim[i])
        time = datetime.datetime.now() - start 
        merge_time.append(time.microseconds)
    
        start = datetime.datetime.now()
        selection_sort(sim[i])
        time = datetime.datetime.now() - start
        select_time.append(time.microseconds)

    return [merge_time, select_time]

x = list(range(1,50))   #getting x values for plot
merge_mean = []
select_mean = []

for i in x:             #need to find the mean runtime of each simulation
   means1 = np.mean(runtime(i)[0])
   merge_mean.append(means1)
   means2 = np.mean(runtime(i)[1]) 
   select_mean.append(means2)

# =============================================================================
# Plotting!
# =============================================================================
 
import matplotlib.pyplot as plt  
plt.plot(x, select_mean, 'g-', label = "Selection Sort")
plt.plot(x, merge_mean, 'b-', label = "Merge Sort")
plt.title("Time Complexity in Sorting Algorithms")
plt.xlabel('N')
plt.ylabel('Average Execution Time')
plt.legend()
plt.show()










