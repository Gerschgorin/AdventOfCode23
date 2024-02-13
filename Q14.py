input = open('Q14_input.txt', 'r').readlines()

cols = []
for j in range(len(input[0])-1):
    cols.append(''.join([input[i][j] for i in range(len(input))]))
    
#print(cols)

def weight(col):
    if col.count('O') == 0 : return 0
    weight0 = 0
    if col.count('#') == 0: 
        for i in range(col.count('O')): weight0 = weight0 + len(col) - i
        return weight0
    beg, end = col.split('#', 1)
    for i in range(beg.count('O')):
        weight0 = weight0 + len(col) - i
    return weight0 + weight(end)

sum = 0
for col in cols:
    sum = sum + weight(col)

print(sum)
    