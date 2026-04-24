for i in range(0,5):
    print(i)

#this right angle triangle
rows = int(input())
for i in range(1,rows):
    for j in range(i):
        print("*",end=" ")
    print()

#rectangle
row = int(input())
colu = int(input())
for i in range(1,rows):
    for j in range(colu):
        print("*",end=" ")
    print()