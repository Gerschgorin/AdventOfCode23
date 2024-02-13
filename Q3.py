import re, numpy as np

def isNotSpecial(i):
    return (i = "." or i.isnumeric() )

def isNotAdjacent(list, i, j):
    adj = [[i-1, j-1],  ]
    return(np.prod(map(isNotSpecial, list[adj])))