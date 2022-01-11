# H.Onur Bahadır - 2140671   
# 19/11/2021 (Poisson distribution fit - Neutrinos from supernovae )

import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import math


def mean_(x,y):
  return (x.dot(y))/np.sum(y)

def poisson(x,m):
  return math.exp(-m)*(m**x) / (math.factorial(x))

#expected values
def fit_poisson(x,m,sum_y):
  exp_y=[]
  for i in x:
    exp_y.append( poisson(i,m)* sum_y)
  return exp_y

#read data
events,intervals=np.loadtxt("Neutrinos.txt",unpack=True,delimiter=",",skiprows=1)

#calculate mean value for poisson distribution
m=mean_(events, intervals) 

#sum of intervals
sum_=np.sum(intervals)

# fit data with poisson distribution
fit=fit_poisson(events,m,sum_)


#print the experimental and expected values
print("Events\tExperiment\tExpected ")
for i in range(len(events)):
  print(f"{int(events[i])}\t{intervals[i]}\t\t{fit[i]:.3f}")

#graphs
fig = plt.figure(figsize=(10, 5))
gs = GridSpec(nrows=1, ncols=2,wspace=0.3)

#
ax0 = fig.add_subplot(gs[:, 0])
ax0.plot(events,intervals,'ro',label="data")
ax0.plot(events,fit,'b--',label="Fit with poisson")
ax0.set_title("Neutrinos from supernovae")
ax0.set_xlabel("Number of Events")
ax0.set_ylabel("Number of in 10s intervals")
ax0.legend()
ax0.grid()


#logarithmic scale  
ax1 = fig.add_subplot(gs[:, 1])
ax1.plot(events,intervals,'ro',label="data")
ax1.plot(events,fit,'b--',label="Fit with poisson")
ax1.set_yscale('log')
ax1.set_title("Neutrinos from supernovae (log scale) ")
ax1.set_xlabel("Number of Events")
ax1.set_ylabel("Number of in 10s intervals")
ax1.legend()
ax1.grid()

plt.show()
