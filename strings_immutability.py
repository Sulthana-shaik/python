s1="Hello"
#s2=s1.concate("World")
print(s1) #Hello
#print(s2)           #Attribute error:str object has no attribute concate

#we can use + operator to join

s3=s1 + "world"
print(s3) #Helloworld


s1="Hello"
print(s1)#Hello
s1=s1 + "World"
print(s1, id(s1)) #HelloWorld 1946855837999830 <- memory address



k1="Python"
k2="Python"
print(k1 , id(k1))      #varaibles in stack memory points towards the same memory lcation
print(k2 , id(k2))
print(k1 is k2)  # is checks thee memory location
print(k1==k2)       #==checks thee content or values r same r not


m1="Python"
m2="pyhton"
print(m1, id(m1))       #varaibles in stack memory points towards the diff memory locatio n as the strings are of different names
print(m2,id(m2))
print(m1 is m2)
print(m1==m2)        



#IMMUTABILITY FEAT .REPLACE()

original_string="Immutable string"
modified_string=original_string.replace("I","i")
print("original string is: ",original_string)
print("modified string is: ",modified_string)
