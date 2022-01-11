# H.Onur Bahadır - 2140671   
# Homework 7  17

import numpy as np 
import matplotlib.pyplot as plt

#reading data
mt1,mt2,fin,lab,hw,Att=np.loadtxt("student.txt",unpack=True,delimiter=",",skiprows=1)

#SXX
def Sxx(x,y):
    x2=0
    for i in range(len(x)):
        x2+=(x[i]*x[i])
    return x2-(np.sum(x)**2)/len(x)   

#SYY
def Sxy(x,y):
    xy=0
    for i in range(len(x)):
        xy+=(x[i]*y[i])
    return xy-(np.sum(x)*np.sum(y))/len(x)

def SSR(x,y):
    return (Sxy(x,y)**2)/Sxx(x,y)

#Total SS
def Syy(x,y):
    syy=0
    m=np.sum(y)/len(y)
    for i in range(len(y)):
        syy+=( (y[i]-m)**2)
    return syy

def SSE(x,y):
    return Syy(x,y)-SSR(x,y)

def MSR(x,y):
    return SSR(x, y)/1

def MSE(x,y):
    return SSE(x, y)/(len(x)-2)

def F(x,y):
    return MSR(x, y)/MSE(x, y)

def r2(x,y):
    return SSR(x, y)/Syy(x, y)

#calculation beta
b=Sxy(mt1,mt2)/Sxx(mt1,mt2)

#calculation alpha
a=(np.sum(mt2)/len(mt2))-b*(np.sum(mt1)/len(mt1))

#get linear fit for every mt1 value to get mt2 fit
linearfit=[]
for i in mt1:
    linearfit.append(a+b*i)

#print F and r^2 values
print("F : ",F(mt1,mt2))

print("r^2 : ",r2(mt1,mt2))

#plot mt1 and m2 with linear fit
plt.scatter(mt1,mt2,label='Scatter Data')
plt.plot(mt1,linearfit,'r-',label=f"Linear Fit : y={a:0.3f}+{b:0.3f}x" )

plt.xlabel("MT1")
plt.ylabel("MT2")
plt.ylim([-20,120])
plt.grid()
plt.legend()
plt.savefig('linear_fit .pdf')
plt.show()


