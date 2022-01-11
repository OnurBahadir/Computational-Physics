# Simpson's Method
import math

# probability density function for Turkish male height 
def h(x):
    return  math.exp(-1*math.pow(x-69,2)/5.6)  / (2.8*(math.pi*2)**0.5)

#Simpson's Method
def simpson(a,b,f,n):
    h=(b-a)/n
    s=f(a)+f(b)
    for i in range(1,n):
        if(i%2==0):
            s+=2*f(a+i*h)
        else:
            s+=4*f(a+i*h)
    return s*h/3

#centimeter to inch
def cm2inch(x):
    return x/(2.54)

b=cm2inch(180)
a=cm2inch(150)
n=40

probability=simpson(a,b,h,n)

print(f"Probability is {probability} ( {probability*100:.2f}% )")
