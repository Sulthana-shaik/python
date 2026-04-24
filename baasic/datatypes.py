a=25
print(a, type(a)) #25 <class 'int'>


a=-80
print(a, type(a)) #-80 <class 'int'>

a=10.8
print(a, type(a)) #10.8 <class 'float'>

a=False
print(a, type(a)) #False <class 'bool'>


a="25"
print(a, type(a)) #25 <class 'str'>

a="10+6y"
print(a, type(a)) #10+6y <class 'str'>

a= 3+ 4j
print(a, type(a)) #(3+4j) <class 'complex'>

#ADDING TWO NUMBERS

num1=15
num2=30
sum_result=num1+num2
#print("The result of the addition:",sum_result) # output=The result of the addition: 45
print("The sum of ",num1, "and",num2,"is:",sum_result ) #The sum of 15 and 30 is: 45

#formatted string it is used to eliminate the confusion of ,'s
print(f"The sum of {num1} and {num2} is: {sum_result}") #output will be the same
#f is reprents as format string



#AREA & PERIMETER OF A RECTANGLE

length=7.5
width=3.2
area=length*width

perimeter=2*(length+width)
print(f"the area of the rectangle with length {length} and width {width} is: {area}")

print(f"the perimeter of the rectangle with length {length} and width {width} is: {perimeter}")



#DISPLAY STUDENT INFO

Roll= 22
Name= "SADIYA"
Stream= "Computer Science"
cgpa= 9.0
print("Roll  number:",Roll)
print("Name:",Name)
print("Stream:",Stream)
print("cgpa:",cgpa)  



name="Raj"
print("Hello," ,name,"!")