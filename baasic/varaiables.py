a=10
b=20
a=40
print(a+b) #output=60 it will take updated a value


a=4.8
print(a+b) # output=24.8


c="10"
d=10
#print(c+d) #output=error,we cant concate str and number ,instead of + we can use ',' inorder to concate str+num then output=10 10
print(c,d)
a=10
A=10
print(a+A) #20   varaibles are treated as diff bcz variables can be treated as case sensitive in python


#we can chain the varaibles ,for multiple variables we can assign single value is called chAINING THE VARAIABLES
x=y=z=100

print(x) #100
print(y) #100
print(z) #100
print(x,y,z) # 100 100 100
print(x+y+z) #300


a , b , c =10 , 20, 30
print(a)#10
print(a,b,c)#10 20 30
print(a+b+c)#60



age=23
print(age)#23
age= age+2
print(age)#25


num1=5
num2=10
num1, num2= num2, num1 # num1 value is stored in num2& num2 value stored in num1 simply like swapping
print(num1,num2) #10 5


a=b=c=0
b=5
print(a,b,c) #0 5 0


price=50
price=price+100
print(price) #150

a=5
b=a
a=10
print(a,b) #10 5

x="10"
y=5
print(x * y) # 10*5=1010101010 bcz here 10 is not an integer its an string


s="abc"*3
print(s) #abcabcabc