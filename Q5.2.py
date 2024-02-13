import re
import numpy as np
input = open("Q5_input.txt", "r").readlines()

#print(input)

seeds_str = input[0].split('seeds: ')[1].split('\n')[0]
seeds = [int(s) for s in seeds_str.split(' ')]
#print(seeds)

seeds_int = [] #list of intervals
for k in range(len(seeds)//2) : 
    seeds_int.append([seeds[2*k], seeds[2*k] + seeds[2*k+1]])
print(seeds_int)

    
def str_to_trip(str):
    a, b, c = str.split(' ')
    return [int(a), int(b), int(c)]
#print(str_to_trip('325190047 421798005 78544109'))

def map(k): # gives k-th map as a list of triplets. START at 0
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

M = len([ l for l in input if 'map' in l]) #number of layers/map
#print(M)

def mapping_inter(list, map):  # map a list of intervals
    result = []
    while list != []:
        progress = False
        [a,b]= list[0]
        for [dest,sour,range] in map:
            if b < sour or a > sour + range: continue   # irrelevant part of the map. Start over the for loop
            if sour <= a and b <= sour + range : # only one map
                result.append([dest + a- sour, dest + b - sour])
                list.pop(0)
                progress = True  
                break  # goes back to the while loop
            if sour <= a < sour + range:   #overlap with a different part of the map
                result.append([dest + a- sour, dest + range])
                list[0] = [ sour+range , b]
                progress = True
                break # goes back to the while loop
        if not progress: # the map didn't do anything
            result.append([a,b])
            list.pop(0)
    return result

# map seeds to locs
locs = seeds_int
for k in range(M):
    locs = mapping_inter(locs, map(k))
#    print(locs)

loc_min = min([locs[i][0] for i in range(len(locs)) ])
print(loc_min)
