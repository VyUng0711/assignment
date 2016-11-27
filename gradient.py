import numpy as np
import math 
import csv 
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
raw = np.genfromtxt('trainingset.csv',delimiter=',')
data = raw[1:-1]
for i in data:
	if i[2]==0:
		i[2]=-1
size = data.shape[0]+1
def scatterPlot(datapoints):
	class0 = []
	class1 = []
	for point in datapoints:
		if point[2] == -1:
			class0.append(point)
		else:
			class1.append(point)
	x0 = []
	y0 = []
	for m in class0:
		x0.append(m[0])
		y0.append(m[1])
	x1 = []
	y1 = []
	for n in class1:
		x1.append(n[0])
		y1.append(n[1])
	plt.scatter(x0,y0,color='red')
	plt.scatter(x1,y1,color='blue')
	#x = np.array(range(-30,30))
	#y = eval("-0.985*x+0.287")
	#y = eval("x**(1/3)")
	#plt.plot(x,y, color = "red", label="y=0.428x+4.085")
	plt.show()
	
#scatterPlot(data)



def gradient_descent(f,dx,dy,dz,start,step,dataset):
	current=start
	error_history=[]
	values_history=[]

	while abs(dx(current,dataset))>0.05 or abs(dy(current,dataset))>0.05 or abs(dz(current,dataset))>0.05:
		error=f(current,dataset)
		error_history.append(error)
		values_history.append(current)
		plt.ion()
		scatterPlot(dataset)
		x=np.array(range(-30,30))
		a=float(-current[0])/float(current[1])
		b=float(-current[2])/float(current[1])
		y=eval("a*x+b")
		plt.plot(x,y, color = "black")
		plt.show()
		plt.pause(0.000005)
		tempx=current[0]-step*dx(current,dataset)
		tempy=current[1]-step*dy(current,dataset)
		tempz=current[2]-step*dz(current,dataset)
		temp=[tempx,tempy,tempz]
		current=temp
	print values_history[-1]
	print error_history[-1]
	xfinal=np.array(range(-30,30))
	afinal=float(-values_history[-1][0])/float(values_history[-1][1])
	bfinal=float(-values_history[-1][2])/float(values_history[-1][1])
	yfinal=eval("afinal*xfinal+bfinal")
	plt.plot(xfinal,yfinal, color = "red")
	plt.show()

	while True:
		plt.pause(0.000005)
	#print error_history
	


		#print "x= ",x
		#print "y= ",y
		#print "z= ",z
		#print "function=", f(x,y,z)
def error_function(vars,dataset):
	m1=vars[0]
	m2=vars[1]
	b=vars[2]
	total_loss=0
	for i in dataset:
		this_loss=math.log(1+(math.e)**(-i[2]*(m1*i[0]+m2*i[1]+b)))
		total_loss+=this_loss
	error=(1/float(dataset.shape[0]+1))*(total_loss)
	return error 

def derivative_m1(vars,dataset):
	m1=vars[0]
	m2=vars[1]
	b=vars[2]
	total_der=0
	for i in dataset:
		this_der=((-i[0]*i[2])*((math.e)**(-i[2]*(m1*i[0]+m2*i[1]+b))))/(1+(math.e)**(-i[2]*(m1*i[0]+m2*i[1]+b)))
		total_der+=this_der
	der_m1=(1/float(dataset.shape[0]+1))*total_der
	return der_m1

def derivative_m2(vars,dataset):
	m1=vars[0]
	m2=vars[1]
	b=vars[2]
	total_der=0
	for i in dataset:
		this_der=((-i[1]*i[2])*((math.e)**(-i[2]*(m1*i[0]+m2*i[1]+b))))/(1+(math.e)**(-i[2]*(m1*i[0]+m2*i[1]+b)))
		total_der+=this_der
	der_m2=(1/float(dataset.shape[0]+1))*total_der
	return der_m2

def derivative_b(vars,dataset):
	m1=vars[0]
	m2=vars[1]
	b=vars[2]
	total_der=0
	for i in dataset:
		this_der=(-i[2]*(math.e)**(-i[2]*(m1*i[0]+m2*i[1]+b)))/(1+(math.e)**(-i[2]*(m1*i[0]+m2*i[1]+b)))
		total_der+=this_der
	der_b=(1/float(dataset.shape[0]+1))*total_der
	return der_b



print "Run gradient descent on the error function to find the classifier"
#print derivative_m1((1,2,3),data)

gradient_descent(error_function, derivative_m1, derivative_m2, derivative_b,(2,3,5), 0.01, data)

#def graph(formula, x_range):
	#x = np.array(x_range)
	#y = eval(formula)
	#plt.plot(x,y)
	#plt.show()

#x = np.array(range(-30,30))
#y = eval("0.428*x+4.085")
#y = eval("x**(1/3)")
#plt.plot(x,y, color = "red", label="y=0.428x+4.085")
#plt.show()






#print gradient_descent(function,dx,dy,dz,[],0.02)

