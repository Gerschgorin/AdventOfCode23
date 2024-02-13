import re
input = open("Q4_input.txt", "r").readlines()

points=[]

for card in input:
    h, tail = re.split(': +', card)
    win_str = re.split(' \| +', tail)[0]
    own_str = re.split(' \| +', tail)[1].split('\n')[0]
    win = re.split('\s+', win_str)
    own = re.split('\s+', own_str)
    n = len(set(own)&set(win))
    points.append(n)

cards= [1]
for i in range(2, 199):
    n = 1+sum(cards[k-1] if points[k-1]>= i-k else 0 for k in range(1, i))
    cards.append(n)

print(sum(cards))
