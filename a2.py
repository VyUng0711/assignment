import random
import math
import matplotlib.pyplot as plt 
import scipy.stats as st
import numpy as np
import time

def in_circle(point,CENTER,RADIUS):
    x = point[0]
    y = point[1]
    center_x = CENTER[0]
    center_y = CENTER[1]
    radius = RADIUS
    return (x - center_x)**2 + (y - center_y)**2 < radius**2

#Estimate Pi by dropping on a rectangular surface with a circle inside
def pi_estimate_rect():
    TIMES_TO_REPEAT = 10**7
    LENGTH = 10
    WIDTH = 7
    RADIUS = 2
    CENTER = [WIDTH/2,LENGTH/2]
    count = inside_count = 0
    pis = []
    sample_size = []
    for i in range(TIMES_TO_REPEAT):
        point = random.uniform(0,WIDTH),random.uniform(0,LENGTH)
        if in_circle(point,CENTER,RADIUS):
            inside_count += 1
        count += 1
        this_pi = ((inside_count/float(count))*LENGTH*WIDTH)/float((RADIUS**2))
        pis.append(this_pi)
        sample_size.append(i)
    print(pis[-1])
    plt.plot(sample_size, pis, color="red")
    plt.xlabel('Sample size')
    plt.ylabel('Value of Pi')
    plt.legend()
    plt.show()

#Estimate Pi by dropping on a square surface with 1/4 of the circle inside. 

def errorbar_version12(N,version):  
    if version == 1: 
         numDarts = [x for x in range(1,N+1)]
    else:
         numDarts = [2**y for y in range(int((math.log(N,2))+1))]
    #We want to start with one dart, so x starts from 1, not 0
    numTrials = 15
    RADIUS = 1
    errors = []
    means = []
    for i in numDarts:
        pis = []
        for j in range(numTrials):
            count = inside_count = 0 
            for k in range(i):
                point = random.uniform(0,RADIUS),random.uniform(0,RADIUS)
                if (point[0])**2 + (point[1])**2 < RADIUS**2:
                    inside_count += 1
                count += 1
            this_pi = 4*(inside_count/float(count))
            pis.append(this_pi)
        SE = np.std(pis)
        z_score = st.norm.ppf(0.975)
        error = SE*z_score
        mean = np.mean(pis)
        means.append(mean)
        errors.append(error)
    print means
    plt.xlabel('Sample size')
    plt.ylabel('Value of Pi')
    plt.errorbar(numDarts, means, errors )
    if version == 1:
        plt.title('Version 1 - Complexity O(N*N)')
    else:
        plt.title('Version 2 - Complextiy O(N*lgN)')
    plt.show()
    

def errorbar_version3():
    p = (math.pi)/4
    N = 10**4
    RADIUS = 2
    CENTER = [0,0]
    count = inside_count = 0
    pis = []
    sample_size = []
    errors = []
    for i in range(1,N):
        point = random.uniform(0,RADIUS),random.uniform(0,RADIUS)
        if (point[0])**2 + (point[1])**2 < RADIUS**2:
            inside_count += 1
        count += 1
        this_pi = 4*(inside_count/float(count))
        SE = math.sqrt((p*(1-p))/i)
        z_score = st.norm.ppf(0.975)
        error = SE*z_score
        pis.append(this_pi)
        errors.append(error)
        sample_size.append(i)
    print(pis)
    plt.xlabel('Sample size')
    plt.ylabel('Value of Pi')
    plt.errorbar(sample_size, pis, errors )
    plt.legend()
    plt.title('Version 3 - Complexity O(n)')
    plt.show()
    
start_time = time.time()
errorbar_version12(10000,1)
time1 = time.time()-start_time
errorbar_version12(10000,2)
time2 = time.time()-time1
errorbar_version3()
time3 = time.time()-time2

