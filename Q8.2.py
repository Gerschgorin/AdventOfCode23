import math

input = open("Q8_input.txt", "r").readlines()

map = []
dirs = input[0].split('\n')[0]
position = []

for line in input[2:]:
    ori, dest = line.split(' = ')
    dest1, dest2 = dest.split('(')[1].split(')')[0].split(', ')
    map.append([ori, dest1, dest2])
    if ori[2] == 'A':position.append(ori)

print(dirs, position, map[:10]) 



def step(pos,dir):
    for ori, dest1, dest2 in map:
        if ori != pos: continue
        if dir == 'L': return dest1
        if dir == 'R': return dest2
        
def step_list(poss, dir):
    out = []
    for pos in poss:
        out.append(step(pos, dir))
    return out

def Zpos(list):
    for i in list:
        if i[2] != 'Z': return False
    return True

count_to_Z = []
L = len(dirs)

#while not Zpos(position):
##for i in range(10):
#    dir = dirs[count % L]
#    print(position)
#    position= step_list(position, dir)
#    count = count+1 

for start in position:
    count = 0
    pos = start
    while pos[2] != 'Z':
        dir = dirs[count % L]
        pos = step(pos, dir)
        count = count+1
    count_to_Z.append(count)
    
    
print(count_to_Z)

print(math.lcm(*count_to_Z))