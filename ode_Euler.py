import matplotlib.pyplot as plt
import numpy as np
import math

def f(x,u):
    return x*x*math.exp(-(u+1))

# 0 < t < 1
t_i=0  
t_f=3

# 1<= i <=100  
N=100
h=0.01

# v(0)=1    
#initial values
t=np.array([0])
v=np.array([1])

for i in range(1,N+1):
    v=np.append(v,v[i-1]+ h*f( v[i-1],t[i-1]))
    t=np.append(t,t[i-1]+h)

plt.plot( t, v, label=r'$\frac{dv}{dt}=1-2*v^{2}-t$ ' )
plt.title( "Euler's Method")
plt.xlabel('t')
plt.ylabel('v(t)')
plt.grid()
plt.legend(loc=1)
plt.show()


