import random 
import numpy as np 
import matplotlib.pyplot as plt
import math 
def selling (number_of_weeks, initial_store_selling, thresholds):
	previous_week = initial_store_selling
	multiple_week = [(1, initial_store_selling)]
	for x in range(number_of_weeks - 1):
		result = []
		for i in thresholds: 
			if previous_week > i:
				result.append(1)
			else: 
				result.append(0)
		#print result
		this_week = sum(result)
		multiple_week.append((x + 2, this_week))
		previous_week = this_week 
	print multiple_week 
	x = [k[0] for k in multiple_week]
	y = [k[1] for k in multiple_week]
	plt.plot(x,y,color='red')
	plt.show()

def selling_advanced (number_of_weeks, initial_store_selling, thresholds):
	previous_week = initial_store_selling
	multiple_week = [(1, initial_store_selling)]
	#Add values for the first three weeks 
	for x in range(2):
		result1 = []
		for i in thresholds:
			if previous_week > i:
				result1.append(1)
			else: 
				result1.append(0)
		this_week = sum(result1)
		multiple_week.append((x+2, this_week))
		previous_week = this_week
	#Add values for the weeks after week 3 
	for y in range(4, number_of_weeks + 1):
		result2 = []
		for i in thresholds:
			average = (multiple_week[y-4][1] + multiple_week[y-3][1] + multiple_week[y-2][1])/3
			distance1 =  abs(multiple_week[y-4][1] - multiple_week[y-3][1])
			distance2 = abs(multiple_week[y-3][1] - multiple_week[y-2][1])
			if average > i and distance1 < 20 and distance2 < 20:
				result2.append(1)
			else: 
				result2.append(0)
		this_week = sum(result2)
		multiple_week.append((y, this_week))
	print multiple_week



def graph_distribution(dist, name):
    plt.hist(dist)
    plt.title(name)
    plt.show()

def main():
	t = int(input("Enter the number of weeks to run the simulation: "))
	try:
		s = int(raw_input("Enter the initial number of stores selling (if not it would be chosen randomly): "))
	except ValueError: 
		s = random.randrange(0,500)
	print "Initial number of stores selling: ", s
	print "Do you want the thresholds to be identical?"

	check = True 
	while check: 
		decision = raw_input("Type y or n: ")
		if decision == 'n':
			r = np.random.random_integers(0,500,500)
			print "Different thresholds for different stores have been automatically generated"
			check = False 
		elif decision == 'y':
			each = int(input("Enter the value of threshold (must be between 0 and 500): "))
			r = [each]*500
			check = False 
		else:
			print "Input is invalid, please enter again"

	#p = selling(t, s, r)
	#print p
	graph_distribution(r, 'Threshold')
	#selling(t,s,r)
	selling_advanced(t,s,r)

main()

