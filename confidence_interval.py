import numpy as np
import matplotlib.pyplot as plt

#import data
number,price,size=np.loadtxt("data.txt",skiprows=1,unpack=True)

#generate (prices/House_size) data 
pdivs=price/size

#error function the part of estimating
def margin_error(data,z):
    return z* (np.std(data)/(len(data)**0.5))

#error function the part of confidence interval
def confidence_interval_error(data,t):
    return t*np.std(data) / (len(data)**0.5)

#z value of %95 
z=1.96 

#t value of %95 confidence
t=2.145

#calculate mean and selling price estimate and print properly

print("Average selling price (using selling prices)")
x1=np.mean(price)
e1=margin_error(price, z)
print(f"{x1:.2f} +- {e1:.2f}")
print( f"{x1-e1:.2f} <= p <=  {x1+e1:.2f}")


print("\nAverage selling price (using selling prices/House size m^2)")
x2=np.mean(pdivs)
e2=margin_error(pdivs, z)
print(f"{x2*np.mean(size):.2f} +- {e2*np.mean(size):.2f}")
print( f"{(x2-e2)*np.mean(size):.2f} <= p <=  {(x2+e2)*np.mean(size):.2f}")


#calculation 95% confidence interval for the price 

print("\nconfidence interval")
x3=np.mean(price)
e3=confidence_interval_error(price,t)
print(f"{x3:.2f} +- {e3:.2f}")
print( f"{x3-e3:.2f} <= p <=  {x3+e3:.2f}")

#Plot prices in histogram 
plt.hist(price)
plt.xlabel("Selling Price (TL)")
plt.ylabel("Frequency")
plt.title("Price Histogram")
plt.grid()
plt.show()






