input = open("Q9_input.txt", "r").readlines()

lists= []
for line in input:
    list = [int(s) for s in line.split('\n')[0].split()]
    lists.append(list)
    
print(lists)

def diff(list):
    out = []
    for i in range(len(list)-1):
        out.append(list[i+1]-list[i])
    return out

def iszero(list):
    for i in list: 
        if i != 0: return False
    return True

def update(list_diff):  # input is a list of lists, with the last one zero
    list_diff[-1].append(0)  # add a term to the zero list
    for i in range(len(list_diff)-2, -1, -1): # start from the last non constant list to the first
        list_diff[i].append(list_diff[i][-1]+list_diff[i+1][-1])
        

sum = 0

for list in lists:
    list_diff = [list]
    while not iszero(list_diff[-1]):
        list_diff.append(diff(list_diff[-1]))
    print(list_diff)
    update(list_diff)
    print(list_diff)
    sum = sum + list_diff[0][-1]

print(sum)    
    