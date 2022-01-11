
def Newton_method(f,df,x,tol=1e-6):
    z=-f(x)/df(x)              # initalize z value   
    while(abs(z)>tol):         # if z is  lower than our tolerance, break loop
        z= -( f(x) / df(x) )   # update z value to changing x
        x += z                 # converge
    return x   

# main function 
# f(x)= x^4 - 6.4x^3 + 6.45x^2 +20.538x - 31.752
def f(x):   
    return ( x*x*x*x -  6.4*x*x*x +  6.45*x*x + 20.538*x - 31.752 )

# derived function 
# df(x)/dx=  4x^3 - 19.2x^2 +12.9x +20.538
def df(x):
    return ( 4*x*x*x - 19.2*x*x  + 12.9*x +  20.538 ) 

#I determine initial value with help of the graph of f(x),it's root is between  -50 and 50
# so i choose 50 as a initial value
x=50
root=Newton_method(f,df,x)
print(f"root is : {root:0.6}")    #print root with 6 significant figure
