input = open('Q15_input.txt', 'r').readlines()

strings = input[0].split(',')

#print(strings[:10], strings[-1])

def hash(str):
    value = 0
    for c in str:
        value = (value + ord(c)) % 256
        value = value * 17 % 256
    return value

sum = 0
for str in strings:
    sum = sum + hash(str)
    
print(sum)
