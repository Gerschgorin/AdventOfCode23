import re
import numpy as np
input = open("Q5_input.txt", "r").readlines()

#print(input)

seeds_str = input[0].split('seeds: ')[1].split('\n')[0]
seeds = [int(s) for s in seeds_str.split(' ')]
#print(seeds)

def str_to_trip(str):
    a, b, c = str.split(' ')
    return [int(a), int(b), int(c)]
#print(str_to_trip('325190047 421798005 78544109'))

def map(k): # gives k-th map as a list. START at 0
    list = []
    map=-1  # increase when 'map' appears
    for line in input:
        if 'map' in line: 
            map+=1
            continue  # next line
        if map==k:  
            if line == '\n': break #end of the map 
            list.append(str_to_trip(line.split('\n')[0]))
    return list

M = len([ l for l in input if 'map' in l])
#print(M)

def mapping(n, map):  # map a number 
    for [dest,sour,range] in map:
        #dest,sour,range = tri
        if sour <= n < sour + range:
            return dest + n - sour
    return n

def full_map(n) : # map a seed to a loc
    for k in range(M):
        n = mapping(n, map(k))
    return n

locs = [full_map(n) for n in seeds]
print(locs)
print(np.min(locs)) 