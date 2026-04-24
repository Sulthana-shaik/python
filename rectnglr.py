r = 5
c = 10
# Rectangle
for rows in range(r):
    for cols in range(c):
        print("*", end="")
    print()


# Right-angled Traingle
for rows in range(r):
    for cols in range(rows * 2 + 1):
        print('*', end="")
    print()


#Hollow Rectangle
for rows in range(r):
    for cols in range(c):
        if rows == 0 or rows == 4:
            print("*", end="")
        elif cols == 0 or cols == 9:
            print("*", end="")
        else:
            print(" ", end="")
    print()