import re
input = open("Q4_input.txt", "r").readlines()

sum = 0


def IsIn(elt, list):
    for i in list:
        if i==elt: return True
    return False


def doublon(l):
    for i in range(1, len(l)-1): 
        if IsIn(l[i], l[:i]): return True
    return False


def nbCommon(l1, l2):
    nb = 0
    for elt in l1:
        if IsIn(elt, l2): nb = nb+1
    return nb

for card in input:
    h, tail = re.split(': +', card)
    win_str = re.split(' \| +', tail)[0]
    own_str = re.split(' \| +', tail)[1].split('\n')[0]
    win = re.split('\s+', win_str)
    own = re.split('\s+', own_str)
    n = len(set(own)&set(win))
    if n != 0: sum += 2**(n-1)

print(sum)