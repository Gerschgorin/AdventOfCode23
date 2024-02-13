import re

input = open("Q2_input.txt", "r")
sum = 0
gameID = 1

def remove(list):
    if list == []: return 0
    else: return int(re.split(' ', list[0])[0])

for line in input: 
    draws = re.split(';', line)
    possible = 1
    
    for set in draws: 
        blue = remove(re.findall(r'\d+ blue', set))
        green = remove(re.findall(r'\d+ green', set))
        red = remove(re.findall(r'\d+ red', set))
    
        if (blue > 14) or (green > 13) or (red > 12): possible = 0
    
    if possible == 1: sum = sum+gameID
    
    gameID += 1 
    
print(sum)
        
