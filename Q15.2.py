input = open('Q15_input.txt', 'r').readlines()

strings = input[0].split(',')

def hash(str):
    value = 0
    for c in str:
        value = (value + ord(c)) % 256
        value = value * 17 % 256
    return value

boxes = [[] for i in range(256)]  # each box is a list of [lbl, focal]

def add(box, txt, nb):
    labels = [box[i][0] for i in range(len(box))]
    if txt in labels:
        ind = labels.index(txt)
        box[ind][1] = nb
    else: box.append([txt, nb])    

def remove(box, txt):
    labels = [box[i][0] for i in range(len(box))]
    if txt in labels:
        ind = labels.index(txt)
        box.pop(ind)

for str in strings:
    if '=' in str:
        txt, nb_str = str.split('=')
        add(boxes[hash(txt)], txt, int(nb_str))
        continue
    txt = str.split('-')[0]
    remove(boxes[hash(txt)], txt)
    
sum = 0
for b, box in enumerate(boxes):
    for l, lense in enumerate(box):
        sum = sum + (1+b)*(1+l)*lense[1]
        
print(sum)