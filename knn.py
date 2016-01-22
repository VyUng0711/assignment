import numpy as np
from random import randrange, random 
import math 
training_set = np.load('knn_data.npy')
n = len(training_set)

import math
#Function calculates distance between two data points. Input: two data points from data set. Output: distance 
def getDistance(instance1, instance2):
	distance = 0
	for x in range(2):
		distance += pow((instance1[x]-instance2[x]), 2)
	return math.sqrt(distance)

#Function returns the neighbors of a certain data point based on distance. Input: data set, tested data point and k. Output: neighbors 
def getNeighbors(trainingSet, testInstance, k):
	distances = []
	for x in range(len(trainingSet)):
		distance = getDistance(testInstance, trainingSet[x])
		if distance != 0:
			distances.append((trainingSet[x], distance))
	sorted_distances = sorted(distances, key=lambda var: var[1])
	neighbors = []
	for x in range(k):
		neighbors.append(sorted_distances[x][0])
	return neighbors
#print training_set[0]
#print getNeighbors(training_set, training_set[0], 2)

#Function returns the predicted label of a certain data point based on its neighbors'labels. Input: neighbors. Output: label 
import operator
def getResponse(neighbors):
	values = [0,1]
	votes = {}
	for x in range(len(neighbors)):
		response = neighbors[x][2]
		if response in votes:
			votes[response] += 1
		else:
			votes[response] = 1
	list_key_value = [[k,v] for k, v in votes.items()]
	if len(list_key_value) == 1:
		result = list_key_value[0][0]
	else:
		if list_key_value[0][1] == list_key_value[1][1]:
			result = randrange(0,2)
		elif list_key_value[0][1] < list_key_value[1][1]:
			result = list_key_value[1][0]
		else:
			result = list_key_value[0][0]
	return result

#print getResponse(getNeighbors(training_set, training_set[0], 3))
#Function returns the predicted set, which consists of all the data points in the training set but with predicted labels. Input: k and training set. Output: predicted set
#Each value of k gives a different prediction
def getPredictions(k, trainingSet):
	instances = [[x[0],x[1]] for x in trainingSet]
	for i in range(len(trainingSet)):
		neighbors = getNeighbors(trainingSet, trainingSet[i], k)
		result = getResponse(neighbors)
		instances[i].append(result)
	predictions = np.array(instances)
	return predictions 

#getPredictions(4, training_set)

#Function returns the accuracy given a training set and a predicted set. 
def getAccuracy(trainingSet, predictions):
	correct = 0
	for x in range(len(trainingSet)):
		if trainingSet[x][2] == predictions[x][2]:
			correct += 1
	return (correct/float(len(trainingSet))) * 100.

#Function returns the accuracy given k and training set. 
def costFunction(k, trainingSet):
	predicted = getPredictions(k, trainingSet)
	accuracy = getAccuracy(trainingSet, predicted)
	return accuracy 
#print costFunction(4, training_set)
#print costFunction(14, training_set)


import matplotlib.pyplot as plt 
#Function creates the scatter plot. Input: set of data points. Output: scatter plot illustrating data points. 
#Label 0: red
#Label 1: blue 
def scatterPlot(datapoints):
	class0 = []
	class1 = []
	for i in range(len(datapoints)):
		if datapoints[i][2] == 0:
			class0.append(datapoints[i])
		else:
			class1.append(datapoints[i])
	x0 = []
	y0 = []
	for m in range(len(class0)):
		x0.append(class0[m][0])
		y0.append(class0[m][1])
	x1 = []
	y1 = []
	for n in range(len(class1)):
		x1.append(class1[n][0])
		y1.append(class1[n][1])
	plt.scatter(x0,y0,color='red')
	plt.scatter(x1,y1,color='blue')
	plt.show()

#scatterPlot(getPredictions(4, training_set))
#scatterPlot(training_set)

#Function finds the optimal k. Input: training set. Output: optimal k 
def optimizeOne(trainingSet):
	result1 = 0
	value1 = 0
	for k in range(1,26):
		new_result1 = costFunction(k, training_set)
		if new_result1 > result1:
			result1 = new_result1
			value1 = k
	final1 = [value1, result1]
	print final1
	n = len(trainingSet)
	k1 = 26
	k2 = n - 1 
	cost1 = costFunction(k1, trainingSet)
	cost2 = costFunction(k2, trainingSet)
	if cost1 > cost2:
		higher = k1
		lower = k2
	else: 
		higher = k2
		lower = k1
	while lower-higher > 1:
		if lower < higher: 
			median = randrange(lower+1, higher) 
		if higher < lower: 
			median = randrange(higher+1, lower)
		cost1 = costFunction(higher, trainingSet)
		cost2 = costFunction(lower, trainingSet)
		test = {}
		cost_median = costFunction(median, trainingSet)
		test[higher] = cost1
		test[lower] = cost2
		test[median] = cost_median 
		sorted_test = sorted(test.iteritems(), key=operator.itemgetter(1), reverse = True)
		print sorted_test
		higher = sorted_test[0][0]
		lower = sorted_test[1][0]
	value2 = higher
	result2 = costFunction(higher, trainingSet)
	final2 = [value2, result2]
	print final2
	final = final1
	if result2 > result1: 
		final = final2
	return final 
#print optimizeOne(training_set)

def optimizeTwo(trainingSet):
	result = [[0,0]]
	count = 0
	for k in range(1, len(trainingSet)-1):
		cost = costFunction(k, trainingSet)
		r = [k, cost]
		if cost > result[-1][-1] or cost == result[-1][-1]:
			result.append(r)
			if count > 0:
				count = count - 1
		else:
			result.append(r)
			count = count + 1
		if count == 3:
			break
	sorted_result = sorted(result, key=lambda var: var[1])
	print sorted_result 
	return sorted_result[-1]
print optimizeTwo(training_set)








	