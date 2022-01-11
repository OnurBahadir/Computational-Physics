import numpy as np 

x=np.array([
    [1,-1,2,1],
    [3,2,1,4],
    [5,-8,6,3],
    [4,2,5,3] ],dtype=np.float64)

b=np.array([1,1,1,-1],dtype=np.float64)

def s_l(x):
    s=[] #scale vector
    l=[] #index vector
    for i in range(len(x)):
        # adding max values in each rows to scale vector
        # signs regarded
        s.append(np.max(abs(x[i])))   
        #adding index
        l.append(i)     
    return s,l

#get scale vector,and index vector
s,l=s_l(x)  
#initialize ratios
ratios=[0,0,0,0]  

for step in range(len(x)-1):
    
    #update ratios
    for r in range(step,len(l)):
        ratios[r]= (abs(x[l[r]][step])/s[l[r]])

    #find max ratio     
    max_in=( np.argmax(ratios[step:len(x)]))
    if(max_in>=step):
    #exchange order for determine pivot  
        l[step],l[max_in]=l[max_in],l[step]
    #forward elimination 
    for i in l[step+1:len(x)]:
        rate=(x[i][step])/(x[l[step]][step])
        rate*=-1
        for j in range(step,len(x)):
            x[i][j] +=  x[l[step]][j]*rate

        b[i] += b[l[step]]*rate
        
# i can't write as a for loop due to complex index notation 
x4= b[l[3]]/x[l[3]][3]
x3=( b[l[2]]-x[l[2]][3]*x4)/(x[l[2]][2])
x2=( b[l[1]]- x[l[1]][3]*x4-x[l[1]][2]*x3) / (x[l[1]][1])

x1=( b[l[0]]-x[l[0]][3]*x4-x[l[0]][2]*x3-x[l[0]][1]*x2)/ x[l[0]][0]

print("x4 : ",x4)
print("x3 : ",x3)
print("x2 : ",x2)
print("x1 : ",x1)

