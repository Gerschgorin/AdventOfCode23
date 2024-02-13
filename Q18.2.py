input = open('Q18_input.txt', 'r').readlines()

instructions = []

for line in input:
    color = line.split('#')[1].split(')')[0]
    dir = int(color[-1])
    dist_hexa = color[:-1]
    dist = int(dist_hexa, 16)
    instructions.append([dir, dist])
#print(instructions) 

# V1:   Les coins des carrés ont des coordonnées entières. 
#       On cherche l'aire du polygone délimité par les les bords des carrés 
#       A = A0 + L0/2 + 1    [dessin]  où
#           A0 est l'aire du polygone P0 déterminé par les centres des carrés
#                (calculable par Green-Riemann à partir des instructions)
#           L0 est le perimètre de ce polygone
#  <=>
# V2:   Les centres des carrés ont des coord entières.
#       On cherche le nombre de points entier contenus dans le polygone P0 (déterminé par les centres des carrés),
#           points du bords inclus
#       N = N_int + N_bord = (N_int + N_bord/2 - 1 ) + N_bord/2 + 1    
#         = A0 + N_bord/2 +1     [Pick's thm]
#       et N_bord = L0

area =0
boundary = 0
i=0
for dir, dist in instructions:
    boundary = boundary + dist
    if dir == 0: 
        i = i+dist
    if dir == 2 : 
        i = i - dist
    if dir == 3 : 
        area = area - i* dist 
    if dir == 1 : 
        area = area + i*dist 
    
print(1+ area + boundary// 2)
