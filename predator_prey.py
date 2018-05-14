import matplotlib.pyplot as plt
import numpy as np
#Input: 
#initial populations for prey (x0) and predator(y0)
#reproduction rate of prey (a)
#rate of predation (b)
#growth rate of predator (c)
#loss rate of predators (d)
#desired final ouput time (T)
#time-step size (h)
#Output:
#Graphs of both predator and prey populations at each time-step on the same plot (blue: prey, green: predator)
#Final predicted population sizes for both predator and prey 
def lotkaVolterra(x0, y0, a, b, c, d, T, h):
    datax = [x0]
    datay = [y0]
    time = [0]
    for i in np.arange(h, T, h):
        time.append(i)
        x = (a*x0 - b*x0*y0)*h + x0
        y = (c*x0*y0 - d*y0)*h + y0   
        # If prey population or predator population is less than zero, the model doesn't make sense
        # If prey population extincts (x = 0), predator population starts to decrease 
        # If predator population extincts (y = 0), prey population will exponentially increase forever 
        #A = x, y 
        if x < 0:
            x = 0 
        elif y < 0:
            y = 0
        else
       
        # if x < 0:
        #    x = 0
        # if y < 0:
            #y = 0 
        
        datax.append(x)
        datay.append(y)
    print "Final predicted population of prey: %s" % x
    print "Final predicted population of predator: %s" % y 
    plt.plot(time, datax, label="prey population")
    plt.plot(time, datay, label="predator population")
    plt.legend(loc='upper left', frameon=False)
    #plt.plot(datax, datay)
    plt.show()
lotkaVolterra(50,15,0.1,0.01,0.001,0.05,100,1)




