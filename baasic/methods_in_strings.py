greet="Hello Good Morning"
#UPPER()   it converts all characters in string to uppercase
print(greet.upper()) #HELLO GOOD MORNING

#LOWER()  it converts all the characters in string to lowercase

print(greet.lower()) #hello good morning


#CAPITALIZE() it converts the 1st character of a string into uppercase and rest to lowercase

print(greet.capitalize()) #Helllo good morning

#TITLE() every character of firts  letter should be capital

print(greet.title()) #Hello Good Morning


#STRIP() it will remove the leading and trailing whitespace from a string but not between space.
s1=" python "
print(s1.strip()) #python
# iit will also remove speciified characters from begiinning and end of the string 

#SPLIT() it will divide a string into list of substrings based on specified separator .if no seperator is specified ,it defaults to splitting  by whitespaces.
#you can also specify a diff seperator
s5="python,is,awesome"
print(s5.split(",")) #['python', 'iss', 'awesome']
print(greet.split()) #['Hello', 'Good', 'Morning']
m1="apple,banana,oraange"
p=m1.split(",")
print(p) #['apple', 'banana', 'orange']

#FIND( ) searches for a specified substring within a string and return the index of its first occurence.
print(greet.find("M")) #11
print("G" in greet) #True
#if theere is no character fouund by defaault it will give -1
#REPLACE() used to replace the occurence of specifieed substring with another substring.
s2="hello world"
print(s2.replace("world","python")) #hello python

#JOIN()  it will accept an array of an individual character and joiin them with specified symbl.

print("-".join(["python", "is", "awesome"])) #python-is-awesome

print("$".join(s2)) #h$e$l4l$0$ $w$$o$r$l$d


#COUNT()   it returnss the occurence of the particular character or word from string 
s6="banaana"
print(s6.count("a")) #4
#STARTSWITH() it will  check the string starts wiith particular character or word from string and return boolean value
print(greet.startswith("He")) #True
#ENDSWITH()  it will check the string end with particular character or owrd from string annd return boolean value
print(greet.endswith("ng")) #true
#ISDIGIT() it will the  string have only digits and return boolean value
print(greet.isdigit()) #false
d1="1234"
print(d1.isdigit()) #true

#ISAPLHA() it will check if the string contain only alphabets and retrun boolean value
print(greet.isalpha()) #false
d2="abc"
print(d2.isalpha()) #true
#ISALNUM() it will check if the string contain both alphabets and numbers and retrun boolean value
print(greet.isalnum()) #false

d3="123ssa"
print(d3.isalnum()) #true
