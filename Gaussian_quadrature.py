import math 

def gaussianQuad(f,a,b):
    x1 = ( (b-a)/2 ) * (-1/(3**0.5)) + (b+a)/2
    x2 = ( (b-a)/2 ) * (1/(3**0.5)) + (b+a)/2
    c1 = (b-a)/2
    c2 = (b-a)/2
    return c1*f(x1)+ c2*f(x2)

# f(x) = e^x * cos(x)
def f(x):
    return math.exp(x)*math.cos(x)


xi=0.5
xf=1.5

print( gaussianQuad(f,xi,xf) )
