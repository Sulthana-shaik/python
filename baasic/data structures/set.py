my_set = {1, 2, 3, 4}
print(my_set)
#❌ No duplicate values
#❌ No indexing (my_set[0] ❌ error)
#✅ Unordered (no fixed position)
#✅ Mutable (you can add/remove items)
#add
s = {1, 2}
s.add(3)
print(s)   # {1, 2, 3}
#remove
s = {1, 2}
s.update([3, 4])
print(s)   # {1, 2, 3, 4}
#set operations
#union
a = {1, 2}
b = {2, 3}
print(a | b)   # {1, 2, 3}
#intersection
print(a & b)   # {2}
#differnce
print(a - b)   # {1}