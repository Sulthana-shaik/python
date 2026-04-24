#program to

# 1. square of numbers
#without list comprehension
sqr = [1,2,3,4,5]
new_sqr = []

for n in sqr:
    new_sqr.append(n * n)
print(new_sqr)

# with list compreshion
sqrr = [1,2,3,4,5]
d = [x * 2 for x in sqrr]
print(d)
#or
lcnew_sqr = [n*n for n in sqrr]
print(lcnew_sqr)

#2.odd numbers only
numbers = [1,2,3,4,5]
odd_numbers = []

for n in numbers:
    if n % 2 != 0:
        odd_numbers.append(n)
print(odd_numbers)
#with
lcodd_numbers = [num for num in numbers if num % 2 != 0]
print(lcodd_numbers)

#3. Convert strings to uppercase
# Without
names = ["ram", "sam", "john"]
upper_names = []
for name in names:
    upper_names.append(name.upper())
print(upper_names)
# With
lcupper_names = [name.upper() for name in names]
print(lcupper_names)

#4. Numbers greater than 10
 #Without
gnumbers = [5, 12, 8, 20, 31]
result = []
for num in gnumbers:
    if num > 10:
        result.append(num)
print(result)
#With
numbers = [1, 5, 12, 18, 3, 25]
lcgnumbers = [num for num in numbers if num > 10]
print(lcgnumbers)
#5. Replace negative numbers with 0
# Without
negnumbers = [2, -3, 5, -1, 7]
result = []
for num in negnumbers:
    if num < 0:
        result.append(0) 
    else:
        result.append(num)
print(result)
#With
result = [ 0 if num < 0 else num for num in numbers]
print(result)
#6. Length of each word
# Without
words = ["apple", "banana", "kiwi"]
lengths = []
for word in words:
    lengths.append(len(word))
print(lengths)
#With
lengths = [len(word) for word in words]
print(lengths)