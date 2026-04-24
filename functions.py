def greet():
    print("Good Morning")
greet() #Good Morning

#ADDITION
def add(a,b):
    print("Addition of a and b is:",a + b)
add(2,3)  #Addition of a and b is: 5



#greet for 1 members
def greet1(name="myfriend"):
    print("Good morning",name)
greet1("sadiya") #Good morning sadiya
greet1("Sulthana") #Good morning Sulthana
greet1() #Good morning myfriend


#assigning default value
def gree(name="my friends"):
    print("Good morning")
gree() #Good morning

#Adding two numbers

def add():
    a = 10
    b=30
    print(a + b)
add() #40


#taking u;ser input
def add():
    a=int(input("Enter value for a:"))
    b=int(input("Enter value for b:"))
    print("The addition of a and b is: ",a+b)
add() #Enter value for a:50    Enter value for b:10    The addition of a and b is: 60


def add():
    a=int(input())
    b=int(input())
    print(a+b)
add()



#1. NO ARGUMENTS WITH RETURN VALUE 

def sqrt():
    num=1
    print(num*num)
sqrt()
#2. NO ARGUMENTS WITH RETURN VALUE

def sqr():
    num=2
    return num * num
print(sqr())

#3. AARGUMENTS WITH RETURN VALUE

def sq(num):
    return num*num
print(sq(10))

#4. ARGUMENTS NO RETURN VALUE

def sqr(num):
    return num*num
print(sqr(10))




# sum
def add():
    a = 10
    b = 20
    print(a+b)
add()
#square
def square():
    a = 4
    print(a*a)
square()

def squ():
    a = int(input("Enter a number: "))
    print("Square of the number is:", a * a)

squ()
#largest num
def largestnum():
    a = 12
    b = 33
    c = 497
    if a > b and a > c:
        print(a)
    elif b > a and b > c:
        print(b)
    else:
        print(c)
largestnum()

# 2nd type
def large():
    a = 35
    b = 23
    c = 4
    return max(a,b,c)
print(large())