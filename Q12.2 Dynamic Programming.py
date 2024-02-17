input = open('Q12_input.txt', 'r').readlines()

map5 = []
for line in input:
    str, nbs = line.split()
    map5.append([(str+'?')*4 + str+'.', tuple([int(c) for c in nbs.split('\n')[0].split(',')]*5)] )   # ALL STRINGS END WITH A .

    
dict_sols = {}

def num_sols(str, nbs, prev):  # prev is the number of # before
    key = (str, nbs, prev)
    if key in dict_sols : 
        return dict_sols[key]
    
    if len(str) == 1: # str is just a .
        if len(nbs) == 0: return prev == 0 # it was a . before
        elif len(nbs) == 1: return prev == nbs[0] # it was a # before and we must fit the last number
        else: return 0
    
    if str[0] == '.' :
        sols = 0
        if prev ==0 : sols = num_sols(str[1:], nbs, 0) # last char was a .
        else : # last char was a #
            try : 
                if (prev !=0 and nbs[0]==prev): 
                    sols = num_sols(str[1:], nbs[1:], 0)  
            except IndexError : # nbs was empty, but prev is non-zero
                pass  

    elif str[0] == '#':
        sols = num_sols(str[1:], nbs, prev+1)
    
    elif str[0] == '?':
        sols = num_sols('.'+str[1:], nbs, prev) + num_sols('#'+str[1:], nbs, prev)
    
    dict_sols[key] = sols
    return sols

print(sum([num_sols(str, nbs, 0) for [str, nbs] in map5]))

