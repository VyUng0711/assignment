# Code for exploring the Central Limit Theorem
# Need NumPy version 1.7 or greater and Matplotlib version

# Uncomment the next line if using IPython for inline plotting
#%matplotlib inline

import numpy as np
import random
import matplotlib.pyplot as plt
import math 

#This function receives inputs which are the population size and the type of population distribution 
#and returns output which is the distribution of the population 
def create_pop(n,form):
    # A
    if form == 'uniform':
        distrib = 1000 * np.random.random_sample((n, ))
    elif form == 'exponential':
        distrib = np.random.exponential(1,1000)
    elif form == 'lognormal':
        distrib = np.random.lognormal(0,1,1000) 
    return distrib

#This function shows the graph of the distribution
def graph_distribution(dist, name):
    plt.hist(dist)
    plt.title(name)
    plt.show()


#This function receives inputs which are a list of sample means, standard error and level of confidence 
#and returns output which is a list of confidence intervals of those samples respectively. 
def intervals(sample_means, se, level):
    #The z-score will be chosen from the dictionary depending on the input of level of confidence
    confidence_level={90:1.64, 95:1.96, 99:2.58}
    z = confidence_level[level]
    sample_intervals = []
    for mean in sample_means:
        lower_bound = mean - se*z
        upper_bound = mean + se*z
        this_interval = (lower_bound,upper_bound)
        sample_intervals.append(this_interval)
    return sample_intervals

#This function receives inputs which are a lists of sample confidence intervels, the population mean and the number of times that we sample 
#and returns output which is the proportion of times the population mean falls within the confidence intervals
def proportion(sample_intervals, population_mean, sample_repeats):
    count = 0
    for x in sample_intervals:
        if x[0] < population_mean < x[1]:
            count+=1
    pro = (count/float(sample_repeats))*100 
    return pro


#This function presents the procedure that we execute with the samples
def sample_procedure(dist):
    global population_mean
    global population_std 
    sample_size = int(raw_input("Enter the sample size:"))
    sample_repeats = int(raw_input("Enter the number of times to repeat the experiment:"))
    level_of_confidence = int(raw_input("Enter the percentage of confidence for the confidence interval: 90, 95 or 99: "))
    sample_means = []
    
    #Everytime we loop through this for-loop, it will create a sample distribution with a sample mean and each sample mean will be stored in the list sample_means 
    for _ in range(sample_repeats):        
        # B
        sample = np.random.choice(dist, (sample_size, ))
        #sample = np.random.choice(dist, (sample_size, ),replace=False)
        this_mean = np.mean(sample)
        sample_means.append(this_mean)

    #"se" is the standard deviation of the sampling distribution or the standard error
    se = np.std(sample_means)
    #"se1" is the standard error that is estimated from the population standard deviation 
    se1 = population_std/float((math.sqrt(sample_size)))
    #"se2" is the standard error that is estimated from the standard deviation of a random sample 
    random_sample = np.random.choice(dist, (sample_size, ))
    random_sample_std = np.std(random_sample)
    se2 = random_sample_std/float((math.sqrt(sample_size)))


    
    
    print "Here's what the sample mean distribution looks like."
    
    plt.hist(sample_means)
    plt.title('Sample Means')
    plt.show()
    
    print "The mean of the sample means is:", np.mean(sample_means)
    print "The standard deviation of the sample means (standard error) is:", np.std(sample_means)


    print "The standard error calculated from the samples - SE = ", se
    prop = proportion(intervals(sample_means, se, level_of_confidence), population_mean, sample_repeats)
    print "Using SE, the proportion of times the population mean falls within the confidence intervals:", prop

    print "The standard error estimated from the population standard deviation - SE1 = ", se1
    prop1 = proportion(intervals(sample_means, se1, level_of_confidence), population_mean, sample_repeats)
    print "Using SE1, the proportion of times the population mean falls within the confidence intervals:", prop1

    print "The standard error estimated from the sample standard deviation - SE2 = ", se2
    prop2 = proportion(intervals(sample_means, se2, level_of_confidence), population_mean, sample_repeats)
    print "Using SE2, the proportion of times the population mean falls within the confidence intervals:", prop2

   
    
    print ""

    #This part we Keep track of all the confidence interval bounds obtained by using the se - standard error calculated from the samples
    correct_intervals = intervals(sample_means, se, level_of_confidence)
    lower = [x[0] for x in correct_intervals]
    upper = [x[1] for x in correct_intervals]
    lower_min = min(lower)
    lower_max = max(lower)
    upper_min = min(upper)
    upper_max = max(upper)
    interval1 = (lower_max, upper_min)
    if interval1[0] < population_mean < interval1[1]:
        print "The population mean falls within the interval between maximum of lower bounds %s and minimum of upper bounds %s" % (lower_max, upper_min)
    else: 
        print "The population mean DOES NOT fall within the interval between maximum of lower bounds %s and minimum of upper bounds %s" % (lower_max, upper_min)
    interval2 = (lower_min, upper_max)
    if interval2[0] < population_mean < interval2[1]:
        print "The population mean falls within the interval between minimum of lower bounds %s and maximum of upper bounds %s" % (lower_min, upper_max)
    else: 
        print "The population mean DOES NOT fall within the interval between minimum of lower bounds %s and maximum of upper bounds %s" % (lower_min, upper_max)

    print ""
   


#####################################

print "First create a (pseudo)-random distribution."
population_size = int(raw_input("Enter a population size:"))
population_type = raw_input("Enter the population distribution: uniform, exponential, or lognormal: ")
print "..."
population = create_pop(population_size,population_type)
population_mean = np.mean(population)
population_std = np.std(population)

print "Here's what the population distribution looks like."
graph_distribution(population, 'Population Distribution')

print "The population mean is:", population_mean

print "For the second step, enter the size of the samples to draw --with replacement-- from the population distribution, and how many times to repeat this procedure in order to create a distribution of sample means."

sample_flag = True

while sample_flag:
    sample_procedure(population)
    print "Perform sampling procedure again? Note that if no, then the population distribution will be lost."
    decision = raw_input("Type y or n:")
    if decision == 'n':
        sample_flag = False
    else:
        print "Doing procedure again."
        

    



