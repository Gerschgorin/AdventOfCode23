from math import sqrt, trunc
import numpy as np

time = [40, 92, 97, 90]
dist = [215, 1064, 1505, 1100]
#time = [7,15,30]
#dist = [9,40,200]
sols=[]

for i in range(len(time)):
    T = time[i]
    d= dist[i]
    root_delta = sqrt(T**2 - 4*d)
    tmin = 1+trunc((T-root_delta)/2)
    tmax = trunc((T + root_delta)/2)
    sols.append(tmax-tmin+1)
print(sols)    
    
prod = np.prod(sols)
print(prod)

