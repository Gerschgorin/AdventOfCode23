import re

input = open("Q2_input.txt", "r")
sum = 0

def remove(list):
    if list == []: return 0
    else: return int(re.split(' ', list[0])[0])

for line in input: 
    draws = re.split(';', line)

    blueMax = 0
    greenMax = 0
    redMax = 0
        
    for set in draws: 
        blue = remove(re.findall(r'\d+ blue', set))
        blueMax = max(blueMax, blue)
        green = remove(re.findall(r'\d+ green', set))
        greenMax = max(greenMax, green)
        red = remove(re.findall(r'\d+ red', set))
        redMax = max(redMax, red)
    
    sum = sum + (blueMax*greenMax*redMax)
        
print(sum)
        
    

