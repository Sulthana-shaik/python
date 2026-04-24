t = (1,3,6)
print(t)
#index -4     -3   -2  -1
#index  0      1   2   3
t1 = ("ramya",5.4,100,'a')
print(t1)
print(t1[0])
print(t1[2])
print(t1[-4])
#immutable
#t1[0] = "mahi"
# we get error because tuple is immutable
#here we get which type
t2 =(3, )
print(t2)
print(type(t2))

#operations
tup = (1,2,3,4)
print(len(tup))
#concatenation
print(t1+tup)

#interview
def name():
    n1 = "ramya"
    n2 = "mahi"
    n3 = "kavya"
    return(n1,n2,n3)
print(name())
#packing and unpacking
Student = ("ramya",23,'cse')
print(Student)
#unpack
name, age, course = Student
print(name)
print(age)
print(course)