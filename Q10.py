map = open("Q10_input.txt", "r").readlines()

def neighb(i, j):
    symb = map[i][j]
    if symb == '|': return [i-1, j], [i+1, j]
    if symb == '-': return [i, j-1], [i, j+1]
    if symb == 'L': return [i-1, j], [i, j+1]
    if symb == 'J': return [i-1, j], [i, j-1]
    if symb == '7' or symb == 'S': return [i, j-1], [i+1, j]
    if symb == 'F': return [i, j+1], [i+1, j]

start = [ [i, line.index('S')] for i, line in enumerate(map) if 'S' in line][0]
start_i, start_j = start

visited = [[0 for i in range(len(map[0]))] for i in range(len(map))]

steps = 1
pos, end = neighb(*start)
print(start, pos)
visited[start_i][start_j] = 1

def step(i,j): 
    visited[i][j]=1
    [n1_i, n1_j], [n2_i, n2_j] = neighb(i,j)
    if visited[n1_i][n1_j] == 0: 
        return [n1_i, n1_j]
    if visited[n2_i][n2_j] == 0:
        return [n2_i, n2_j]

while pos != end : 
    print(pos)
    pos = step(*pos)
    steps = steps+1
    
print((1+steps)//2)