input = open('Q20_input.txt', 'r').readlines()

def replace(char):
    if char == '.': return 0
    if char == '#': return -1
    if char == 'S': return 1

def replace_noS(char):
    if char == '.': return 0
    if char == '#': return -1
    if char == 'S': return 0


map = [[replace(char) for char in input[i][:-1]] for i in range(len(input)) ]
empty = [[replace_noS(char) for char in input[i][:-1]] for i in range(len(input)) ]

def check_neighb(i, j, m):
    try : S = (m[i-1][j] == 1)   # la case sud a est visitée
    except: S = False 
    try : N = (m[i+1][j] == 1)   # la case sud a est visitée
    except: N = False 
    try : W = (m[i][j-1] == 1)   # la case sud a est visitée
    except: W = False 
    try : E = (m[i][j+1] == 1)   # la case sud a est visitée
    except: E = False 
#    print(S, W, N, E)
    return S or W or N or E



def update(m):
    updated = [[replace_noS(char) for char in input[i][:-1]] for i in range(len(input)) ]
    for i, line in enumerate(updated):
        for j, elt in enumerate(line):
            if elt == -1 : continue  # can't visit there
            if check_neighb(i, j, m): 
#                print(i, j)
                updated[i][j] = 1
#                print(m)
    return updated

for k in range(64):
    map = update(map)
    print(map)
#map2 = update(map1)
#print(map2)

#print(map[10][8])
#print(check_neighb(10, 8, map))    

print(sum([line.count(1) for line in map]))