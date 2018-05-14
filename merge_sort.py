import matplotlib.pyplot as plt 
from random import randint
import numpy as np
import time 
import math
import pandas as pd
#Generate a list with m random elements 
def rand_list(m):
    lis = []
    for _ in range(m):
        lis.append(randint(-1000,1000))
    lis.sort(reverse=True)
    return lis

def merge(lefthalf,righthalf):
    i = 0 
    j = 0
    sortlst = []
    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j] :
            sortlst.append(lefthalf[i])
            i=i+1
        else:
            sortlst.append(righthalf[j])
            j=j+1

    while i < len(lefthalf):
        sortlst.append(lefthalf[i])
        i=i+1

    while j < len(righthalf):
        sortlst.append(righthalf[j])
        j=j+1
    return sortlst

def TwoWayMergeSort(alist):
    #print("Split",alist)
    if len(alist) > 1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        #print ("L: ", lefthalf)
        righthalf = alist[mid:]
        #print("R: ",righthalf)
        lefthalf = TwoWayMergeSort(lefthalf)
        righthalf = TwoWayMergeSort(righthalf)
        alist = merge(lefthalf,righthalf)
    return alist


def ThreeWayMergeSort(alist):
    if len(alist)>1:
        size = int(round(len(alist)/float(3)))
        size3 = len(alist)-2*size
        temp1 = [alist[a] for a in range(size)]
        temp2 = [alist[b] for b in range(size,2*size)]
        temp3 = [alist[c] for c in range(2*size,len(alist))]
        temp1 = ThreeWayMergeSort(temp1)
        #print "Temp1: %s" % temp1
        temp2 = ThreeWayMergeSort(temp2)
        #print "Temp2: %s" % temp2
        temp3 = ThreeWayMergeSort(temp3)
        #print "Temp3: %s" % temp3
        alist=merge(merge(temp1,temp2),temp3)
    return alist

def insertionSort(alist):
    for i in range (1,len(alist)):
        key = alist[i]
        j = i-1
        while j >= 0 and alist[j] > key:
            alist[j+1] = alist[j]
            j = j - 1
        alist[j+1] = key
    return alist

def AugmentedMergeSort(alist):
    if len(alist)>1:
        size = int(round(len(alist)/float(3)))
        size3 = len(alist)-2*size
        temp1 = [alist[a] for a in range(size)]
        temp2 = [alist[b] for b in range(size,2*size)]
        temp3 = [alist[c] for c in range(2*size,len(alist))]
        if len(temp1) <= 4:
            temp1 = insertionSort(temp1)
        else:
            temp1 = AugmentedMergeSort(temp1)
        #print "Temp1: %s" % temp1
        if len(temp2) <= 4:
            temp2 = insertionSort(temp2)
        else:
            temp2 = AugmentedMergeSort(temp2)
        #print "Temp2: %s" % temp2
        if len(temp3) <= 4:
            temp3 = insertionSort(temp3)
        else:
            temp3 = AugmentedMergeSort(temp3)
        #print "Temp3: %s" % temp3
        alist=merge(merge(temp1,temp2),temp3)
        #print alist
    return alist


randomlist = rand_list(10)

#simple = [1,2,0,6,3,8,7,5,4,5,10,16,13]
#print TwoWayMergeSort(simple)
#print ThreeWayMergeSort(simple)
#print AugmentedMergeSort(simple)


#Compare running times of three types of Merge Sort with list size incremented from 2^0 to 2^14.
size = []
allruntime1 = []
allruntime2 = []
allruntime3 = []
list_sizes = [2**i for i in range(15)]
for m in list_sizes:
    randoms1 = []
    randoms2 = []
    randoms3 = []
    #At each list size, regenerate 10 times to calculate the average running time of each algorithm. 
    for n in range(10):
        test = rand_list(m)
        start_time1 = time.time()
        TwoWayMergeSort(test)
        randoms1.append(time.time()-start_time1)
        start_time2 = time.time()
        ThreeWayMergeSort(test)
        randoms2.append(time.time()-start_time2)
        start_time3 = time.time()
        AugmentedMergeSort(test)
        randoms3.append(time.time()-start_time3)
    runTime1=np.mean(randoms1)
    runTime2=np.mean(randoms2)
    runTime3=np.mean(randoms3)
    allruntime1.append(runTime1)
    allruntime2.append(runTime2)
    allruntime3.append(runTime3)
    size.append(m)
   
plt.plot(size, allruntime1, color="red", label="Two-way MS")
plt.plot(size, allruntime2, color="blue", label="Three-way MS")
plt.plot(size, allruntime3, color="green", label="Augmented Three-way MS")
plt.xlabel('Size of list (number of elements)')
plt.ylabel('Running Time (seconds)')
plt.legend()
plt.show()

data = {'List Size': list_sizes,
        'Two-way Merge Sort': allruntime1,
        'Three-way Merge Sort': allruntime2,
        'Augmented Three-way Merge Sort': allruntime3}
df = pd.DataFrame(data, columns = ['List Size','Two-way Merge Sort','Three-way Merge Sort','Augmented Three-way Merge Sort'])
df.to_csv('runtimes.csv')


