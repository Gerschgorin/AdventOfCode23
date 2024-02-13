map = open("Q11_input.txt", "r").readlines()

gal = [] 

empty_lines = []
for i in range(len(map)):
    if map[i].find('#') == -1: empty_lines.append(i)
    gal = gal + [[i, j] for j in range(len(map[i])) if map[i][j] == '#']
    
empty_col = []
for j in range(len(map[0])-1):
    col = [map[i][j] for i in range(len(map))]
    if '#' not in col: empty_col.append(j)
    
#print(gal, empty_lines, empty_col)

sum = 0

for gal1 in gal:
    for gal2 in gal:
        i1, j1 = gal1
        i2,j2 = gal2
        sum = sum +  abs(i1-i2) + abs(j1-j2) + 999999*len([i for i in empty_lines if min(i1, i2) < i < max(i1, i2) ]) + 999999*len([j for j in empty_col if min(j1, j2) < j < max(j1, j2) ])
    
print(sum//2)