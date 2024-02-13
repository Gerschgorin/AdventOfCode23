input = open("Q8_input.txt", "r").readlines()

map = []
dirs = input[0].split('\n')[0]


for line in input[2:]:
    ori, dest = line.split(' = ')
    dest1, dest2 = dest.split('(')[1].split(')\n')[0].split(', ')
    map.append([ori, dest1, dest2])
    
#print(dirs, map[:10])

position = 'AAA'

def step(pos,dir):
    for ori, dest1, dest2 in map:
        if ori != pos: continue
        if dir == 'L': return dest1
        if dir == 'R': return dest2

#print(step('BQV', 'R'))

count = 0
L = len(dirs)

while position != 'ZZZ':
#for i in range(10):
    dir = dirs[count % L]
    print(position)
    position= step(position, dir)
    count = count+1

print(count)
