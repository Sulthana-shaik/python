#Strings are treated as object in Python 
#Strings are enclosed with single,double,triplee quotes.
#Strings are also called as group/sequence/set of characters.

str1='Sadiya'
str2="sulthana"
str3='''Shaik''' #multi line string
str4='''''Ammu'''''#multi line string
''' str5='i'm Sadiya' '''
#here the above  string gets confused wheether it should take i or i'm sadiya thats you in this sceniors we have to mention "i'm Sadiya" like this.
print(type(str3)) #<class 'str'>
str6='''"i'm sadiya from "pileru" ''' 
print(str6)
#above code pileru ,we have given " " so that we have to enclose the whole sentence in ''' to eliminate the confusion we can use  escape sequence character that is ntng but \

str7=" i'm sulthana from \"pileru\" "
print(str7)



str8=" hello ? i'm anusha from \"kodnest\" how about you"
print(str8)

#to get a ouput in line by line  we have to give ''' ''' or """ """ multi line formate
s='''hello
my name is
sulthana'''
print(s)

k='i\'m sadiya'
print(k)



#STRING SLICING 

# it allows you to extract  a part of string  by using syntax  string[start:end]
#[-6 -5 -4 -3 -2 -1]
#[k o d n e s t]
#[0 1 2 3 4 5 6]
A="kodnest"
print(A[5]) # it will access by using index num, starting with 0 in left to right is called positive slicing and in reverse it will start with -1 from right to left called as negetive slicing.
print(A[0:3]) # end=n-1 so the output is kod
print(A[:4]) #if u didnt give any start value it will consider it as 0  ,so the output is kodn
print(A[2:6]) #output=dnes
print(A[3:7]) #output=nest
print(A[3:9]) #output=nest

#negative slicing

print(A[-2]) #output=s
print(A[-7:-3]) #kodn
print(A[-7:-4]) #kod
print(A[:-2]) #kodne
print(A[-5:-1]) #dnes
print(A[-4:]) #nest if we give [-4:0] it wont give anny output will be empty string " " bcz negative indexing starts with -1.
print(A[3:]) #nest  whenever we dont given thhe  end value also it  will consider the entire string upto  last letter.

#Additionally we can   specify the step value using syntax as string[Start:end:step]


#* positive stepcount by default is 1  here the stepcount is{end=-1}

print(A[0 : 7 : 1]) # kodnest here step value =1 and stepcount =-1 so +1-1=0 it woont skip any value.
print(A[0:7:2]) #kdet here 2-1=1  the skipvalue is 1.
print(A[2:5:2]) #de here 2-1=1 the skipvalue is 1.
print(A[:6:1]) #kodnes
print(A[:6:2]) #kde
print(A[::3]) #knt here 3-1=2 the skip value is 2
print(A[3::2]) #ns



#*negative stepcount by default -1 here the stepcount is {end=+1}

print(A[::-1]) #tsendok  heree stepcount=-1+1=0 skipvalue=0
print(A[-6::-1]) #ok here stepcount=-1+1=0 skipvalue=0
print(A[-5:-1:-2]) #" " empty string bcz the string in -ve sliciing taraverse in righ to left.  here stepcount=-2+1=1 skipvalue=1
print(A[-7::-3]) # k here stepcount=-3+1=2 skipvalue is 2
print(A[-2::-1]) # sendok here stepcount=-1+1=0 skipvalue is 0
print(A[-5:-2]) #dk here stepcount=-2+1=1 skipvalue is 1
print(A[-3:-8:-2])# edk here stepcount=-2+1=1 skipvalue is 1 
print(A[::-2]) # tedk here stepcount=-2+1=1 skipvalue is  1



