s1 = 'ramya';
print(s1)
s2 = "Ramya";
print(s2)
s3 = '''RAmya'''
print(s3)
s4="""RAMya"""
print(s4)
s5 = "I'm Ramya"
print(s5)
s6 = """ hello,
     how are you?
     thankyou! """
print(s6)
s = """ hello,how are you?thankyou! """
print(s)
# adding to strings
s7 = "sri"
s7 = s7 + "Ramya"
print(s7)
print(id(s7))
s8 ="hello"
s9 = s8 + "world"
print(s8, id(s8))
print(s9, id(s9))
r1 = "python"
r2 = "python"
print(r1, id(r1))
print(r2, id(r2))
print(r1 is r2)

#list
a = [1,2,3]
b = a
c = [1,2,3]
# is -->adress
# => content
print(a is b)#true
print(a is c)#false
print(a == c)#true

e1 = "True"#string
res = bool(e1)#t/f
print(e1)#true
print(type(res))