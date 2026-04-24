print("Please enter your name")
name=input()
print("Entered name is:",name)


#instead of this we can directly print the userinput

age=input("enter age ")
print("Entered age is: ",age)



#Adding 2 numbers using userinput
num1=input("Enter number 1: ")
num2=input("Enter number 2: ")
num=num1+num2
print(f"The addition of {num1} and {num2} is: {num}") #the output will be like 28 
#because the enterd numbers it wll consider as strings "2"+"8"=28 it is by default the input() retruns the output as string so that we have to typecaste
#to covert the input into different data types we use type casting functions like int(),float(),bool() etc..,
#it will take the input as string and convert to a integer.
#TYPECASTING means converting  a valu e from one data type to another data type
#we can typecaste in 2ways: 1st type is:
num1=int(input("Enter number 1: "))
num2=int(input("Enter number 2: "))
num=num1+num2
print(f"The addition of {num1} and {num2} is: {num}") #output=6  [2+4=6]
  #2nd way:
num1=input("Enter number 1: ")
num2=input("Enter number 2: ")
num=int(num1)+int(num2)
print(f"The addition of {num1} and {num2} is: {num}") #output=7 [2+5]

#FIRST WAY is better


#Collecting cgpa

cgpa=float(input("Enter cgpa "))
print(cgpa)


#Area of Rectangle
a=int(input("length is "))
b=int(input("width is "))
area=a*b
print("area of rectangle is: ")



#Grreetinng
user_name=input()
user_age=input()
print(f"Hello {user_name}! you are {user_age} yearrs old")      #when the requriments gives 2 or more sample outputs we make use of input()-->prompt
#output will be as their requirment    