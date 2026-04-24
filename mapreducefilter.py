print("squares")
def multiply_list(lst, num):
    return [i * num for i in lst]

numbers = [1, 2, 3, 4, 5]
print(multiply_list(numbers, 2))
#-----------------map-----------
def square(x):
    return x * 2
n = [1,2,3,4,7]
squares = list(map(square, n))
print(squares)
#or ---lamda--
n = [2,3,4,5]
s = list(map(lambda x: x * 2, n))
print(s)
print("----------------")

print("fliter")
# even numbers
# Function to get even numbers from list
def get_even_numbers(lst):
    even_list = []
    for i in lst:
        if i % 2 == 0:
            even_list.append(i)
    return even_list

# Given list
numbers = [1, 2, 3, 4, 5]

# Function call
result = get_even_numbers(numbers)

print("Even numbers:", result)
#or
def is_even(x):
    return x %2 == 0
num = [1,2,3,4,5]
ev = list(filter(is_even, num))
print(ev)
#or
numb =[1,2,3,4,5]
eve = list(filter(lambda x: x % 2 ==0, numb))
print(eve)
#reduce
print("--------------")
#sum of numbers
numbers = [1, 2, 3, 4, 5]

total = 0
for x in numbers:
    total = total + x

print(total)
#or
# Function to calculate sum of list
from functools import reduce

def add(a, b):
    return a + b

numbers = [1, 2, 23, 4, 5]

total = reduce(add, numbers)
print(total)
#lamda
from functools import reduce
numbers = [1, 24, 23, 4, 5]
total = reduce(lambda a,b: a+ b,numbers)
print(total)