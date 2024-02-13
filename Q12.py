import re

input = open('Q12_input.txt', 'r').readlines()

#def convert(str):
#    out = []
#    for char in str:
#        if char == '.': out.append(1)
#        if char == '#': out.append(-1)
#        if char == '?': out.append(0)

map = []
for line in input:
    str, nbs = line.split()
    map.append([str, [int(c) for c in nbs.split('\n')[0].split(',')]] )
    
def admiss(str, nbs): #test a string with . and #
    striped = str.strip('.')
#    print(striped)
    splited = re.split(r'\.+', striped)
#    print(splited)
    return nbs == [len(w) for w in splited]

#print(admiss('.##...##.', [1,2]))    

def all_poss(str): #return list of string
    if str.count('?') == 0 : return [str]
    beg, end = str.split('?', 1)
    return [beg+'.'+all_end for all_end in all_poss(end)]+[beg+'#'+all_end for all_end in all_poss(end)]

sum = 0 
for str, nbs in map:
    for poss in all_poss(str):
        if admiss(poss, nbs):
            print(str, poss, nbs)
            sum = sum+1
        
print(sum)
