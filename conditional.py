#write a program to check whther the given number is positive

num=2
if (num==2):
    print("Positive number")
else:
    print("Negative number") #Positive number

#Taking user input
num1=int(input("Enter Any number as ur wish: "))
if(num1>0):
    print("Entered number is Positive ")
else:
    print("Entered number is Negative")




#write a program to check if a student has passed the exm pass mrks=40

passmarks=50
if(passmarks>=40):
    print("Student has passed the exm")
else:
    print("Student has failed the exm")

#Taking user input
passmarks=int(input("Enter the pass marks:"))
if(passmarks>=50):
    print("Student is passed")
else:
    print("student is failed")
    
#write a code to check if a number is even or odd
num1=int(input("Enter a number:"))
if(num1%2==0):
    print("number is even")
else:
    print("number is odd")


#write a code to check a person is eligible to vote or not .eligible if age is >=18
age=23
if age>=18:
    print("Eligible to vote")
else:
    print("Not eligible")

#write a program to determine the grade of a student based on maarks
#90 and above -->A
#75 to 89 ->B
#60 to 74 ->C
#below 60 ->fail
marks=72
if marks >=90:
    print("Grade A")
elif marks >=75:
    print("Grade B")
elif marks >=60:
    print("Grade C")
else:
    print("Fail")

# program to display largest of three numbvers
x,y,z=10,20,30
if x>y and x>z:
    print("Largest:",x)
elif y>z:
    print("Lagrgest:",y)
else:
    print("Laargest",z)
#taking userinput
x=int(input("Enter first number:"))
y=int(input("Enter second number:"))
z=int(input("Enter third number:"))
if x>y and x>z:
    print("Largest:",x)
elif y>z:
    print("Lagrgest:",y)
else:
    print("Laargest",z)

#NESTED IF
#write a program to check if a number is positivee
#if positive,then check if its even or odd
num=8
if(num>0):
    print("Positive number")
    if(num %2 ==0):
        print("Even number")
    else:
        print("Odd number")
else:
    print("Negative number")

    