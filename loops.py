# looping statements for/while

# 01234
for i in range(5):
    print(i)


#while   
i = 0 
while i <= 4:
    print(i)
    i += 1

#even numbers 2,4,6,8,10
for num in range(1, 11):
    if num % 2 == 0:
        print(num)

# jump control statements
# 1-6
# break  = 3
for i in range(1, 6):
    if i == 3:
        break
    print(i)

    # continue
for i in range(0, 6):
    if i == 4:
        continue
    print(i)

def square(n):
    return n * n
print(square(4))

# pass 
for i in range(0, 6):
    pass
def add():
    pass
add()