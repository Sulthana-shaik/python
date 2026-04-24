#Lists - [],ordered , homo/hetero, indexing, mutuble
#homogeneous
stu_list=["Rajesh", "Darshan", "megha"]
stu_list.append("Nikhil")
stu_list.append("Rajesh")
stu_list.insert(1, "Rahul")
stu_list.pop(1)
#stu_list.remove("Megha")
stu_list[1]="Rahul"
stu_list.remove("Rajesh")

print(stu_list[1])
stu_list.sort()
#print(stu_list[3])
print(stu_list)
print(len(stu_list),type(stu_list))
#Heterogeneous
stu_info=["Darshan",8.9,23,True]
print(stu_info)


numbers = [10, 20, 30, 40]
print(numbers)

data= [10, 3.5, "jyothi", True]
print(data)
#accessing data - index starts
print(data[2])
data[2] = "mahaesh"
print(data)
#adding elements
numbers = [10, 20, 30, 40]
numbers.append(50) #end
print(numbers)
numbers.insert(1, 70) #index[10,70, 20, 30, 40]
print(numbers)

#remove elements
numbers.remove(70)#value
print(numbers)
numbers.pop(4) #index
print(numbers)
print(len(numbers)) 

numbers.append(100)
for num in numbers:
# print(num)# print same line
 print(num, end=" ")

#extend(
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1) #[1, 2, 3, 4, 5, 6]

list3 = [4, 6, 8,1, 9]
print(list3)
list3.sort() #assending order
list3.reverse() #desending order
print(list3)

words = input().split()
print(words)

fruits = ["apple","mango","banana"]
print(fruits.index("banana"))
print(fruits.count("banana"))

fruitslist = fruits.copy()
print(fruitslist)
#delete the friutlist
#del fruitslist
#print(fruitslist)
