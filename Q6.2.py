from math import sqrt, trunc

T = 40929790
d = 215106415051100

root_delta = sqrt(T**2 - 4*d)
tmin = 1+trunc((T-root_delta)/2)
tmax = trunc((T + root_delta)/2)

print(tmax-tmin+1)