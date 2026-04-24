#no arguments +  no return value
def add():
    a = 30
    b = 25
    print(a+b)
add()
# no arguments + retuen value
def add():
    c = 44
    d = 22
    return (c+d)
print(add())
# argumnets + no return value
def add(x,y):
    print(x+y)
add(555,7)
# argumnets +  return value
def add(av,bv):
    return av+bv
res = add(282,99)
print(res)

# finding a cube of number
#no arguments +  no return value
def cube():
    a = 3
    print(a*a*a)
cube()
# no arguments + retuen value
def cube():
    a = 4
    return(a*a*a)
print(cube())
#argumnets + no return value
def cube(a):
    print(a*a*a)
cube(7)

# argumnets +  return value
def cube(a):
    return a*a*a
result = cube(3)
print(result)