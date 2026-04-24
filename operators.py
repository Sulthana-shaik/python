#---Arithmetic oprators-------


x=15
y=4

print(x + y) #19
print(x - y) #11
print(x * y) #60
print(x / y) #3.75  divison always gives output as qutiont which ,means complete number
print(x % y) #3     modulus alwys gives the output as reminder
print(x ** y) #50625   exponential output means power of the input
print(x // y)  #3    floor division gives output as nearest value or rounded to int value




#-----ASSINGMENT OPERATOR-----

x=10
print("starting vale: x=",x) #10


x=10
print("After =  :" ,x) #10

x += 10
print(x) #20

x -= 10
print(x) #10

x *= 10
print(x) #1100

x /= 10
print(x) #10.0

x //= 10
print(x)  #1.0

x %= 10
print(x)  #1.0

x **= 10
print(x) #1.0

x=6
print("Reset x=",x) #resetting the value from 1.0 to 6 so the x value is 6


x &= 6
print(x) #6

x |= 6
print(x)  #6

x ^ 6
print(x) #6

x <<= 6
print(x) #384

x >>= 6
print(x) #6




#---COMPARISON OPERATOR---

x=3
y=2

print(x == y) #false

print(x != y) #true

print(x > y) #true

print(x < y) #false 

print(x >= y) #true

print(x <= y) #false


print("--------python allows you to chain the comparison operator------")
x=5
print(1 < x < 10) #true
print(1 < x and x < 10) # true



#------LOGICAL OPERATORS------
a=True
b=False
print(a and b) #false

print(b and a) #false

print(a or b) #true
print(b or a) #true

print(not b) #true
print(not a) # false


x=15
y=10

print((x>y) and (y<x)) #true

print((x<y) or (x>y)) #true

print(not (x==10)) #true



#----IDENTITY OPERATOR-----
x=['apple','banana']
y=['apple','banana']
z=x
print(z == x)  #checks value and output=true
print(z is y) # checks for pointing to same  object or not output=false


#---MEMBERSHIP OPERATOR---

a=["apple","banana"]
b=["guva","orange"]

print("pineapple" not in a) #true
print("guva" in b) # true
print("guva" in a) #false


#-----BITWISE OPERATOR----
a = 5
b = 3

print(a & b) #1

print(a | b) #7

print(a ^ b) #6

print( ~ a) #-6

print(a << b) #40

print(a>>b) #0