import numpy

input = open("Q1_input.txt", "r") 
sum = 0


for line in input:
    i1 = line.find("one")
    i2 = line.find("two")
    i3 = line.find("three")
    i4 = line.find("four")
    i5 = line.find("five")
    i6 = line.find("six")
    i7 = line.find("seven")
    i8 = line.find("eight")
    i9 = line.find("nine")
    I = numpy.array([i1, i2, i3, i4, i5, i6, i7, i8, i9])
    I[I==-1] = 100000
    i0 = min(I)
    a0 = 1+numpy.argmin(I)

    j1 = line.rfind("one")
    j2 = line.rfind("two")
    j3 = line.rfind("three")
    j4 = line.rfind("four")
    j5 = line.rfind("five")
    j6 = line.rfind("six")
    j7 = line.rfind("seven")
    j8 = line.rfind("eight")
    j9 = line.rfind("nine")
    j0 = max(j1, j2, j3, j4, j5, j6, j7, j8, j9)
    b0 = 1+numpy.argmax([j1, j2, j3, j4, j5, j6, j7, j8, j9])

    print(a0, i0, j0, b0)    
    i=-1 #index of first number 
    j=-1 #index of last number
    k=0
    for l in line:
        if l.isnumeric():
            j = k
            if i == -1:
                i = k
        k=k+1

    if i<i0:
        a=line[i]
    else: a=a0
    if j>j0: b=line[j]
    else: b= b0
    
    sum = sum + 10*(int(a)) + int(b)
    
print(sum)