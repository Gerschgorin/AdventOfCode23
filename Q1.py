import numpy

input = open("Q1_input.txt", "r")  #THERE IS NO 0
sum = 0

for line in input:
    a=-1
    b=-1

    for i in line:
        if i.isnumeric():
            b = i
            if a == -1:
                a = i

    sum = sum + int(a+b)

print(sum)

sum2 = 0

for line in input:
    print(0)


for line in input:
    a=-1
    b=-1
    i1 = line.index("one")
    i2 = line.index("two")
    i3 = line.index("three")
    i4 = line.index("four")
    i5 = line.index("five")
    i6 = line.index("six")
    i7 = line.index("seven")
    i8 = line.index("eight")
    i9 = line.index("nine")
    i0 = min(i1, i2, i3, i4, i5, i6, i7, i8, i9)
    a0 = 1+numpy.argmin(i1, i2, i3, i4, i5, i6, i7, i8, i9)

    j1 = line.rindex("one")
    j2 = line.rindex("two")
    j3 = line.rindex("three")
    j4 = line.rindex("four")
    j5 = line.rindex("five")
    j6 = line.rindex("six")
    j7 = line.rindex("seven")
    j8 = line.rindex("eight")
    j9 = line.rindex("nine")
    j0 = max(j1, j2, j3, j4, j5, j6, j7, j8, j9)
    b0 = 1+numpy.argmax(j1, j2, j3, j4, j5, j6, j7, j8, j9)

    print(a0, i0, j0, b0)    
    for i in line:
        if (i < i0 or i>j0) and i.isnumeric():
            b = i
            if a == -1:
                a = i

    sum = sum + int(a+b)


input.close()