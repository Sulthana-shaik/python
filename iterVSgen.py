print("normal-function")
#def count_num(n):
# numbers = []
# count = 1
#   while count <= n:
#  numbers.append(count)
#       count+=1
#   return numbers
# usernum = int(input("enter the count"))
# for n in count_num(usernum)
#   print(n)

print("-----genrator function----")   
def count_num(n):
    count = 1
    while count <= n:
        yield count
        count+=1
usernum = int(input("enter"))
for n in count_num(usernum):
    print(n)
