
#Forward Difference  
def fd(f,x,h):
    return ( f(x+h)-f(x) ) / h 

#Modified Forward Difference
def mfd(f,x,h):
    return  ( -1*f(x+2*h) + 4*f(x+h)-3*f(x)) / (2*h)

#data in function
def f(x):
    data={
        0 : 13.5,
        1.25 : 12.0,
        2.5 : 10.0
    }
    return data[x]

#Constants
k = 3.5e-7  # m^2 /s)
p = 1800    # kg/m^3 )
C = 840     # J/ kg C)

#Heat flux in Forward Difference
q1= -1 * k*p*C * fd(f,0,1.25) 

#Heat flux in Modified Forward Difference
q2= -1 * k*p*C * mfd(f,0,1.25) 


print(f'Heat flux in fd : {q1:.5f} kg/s^3')

print(f'Heat flux in mfd : {q2:.5f} kg/s^3')




