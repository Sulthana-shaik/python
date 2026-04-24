class Student:
    institute = "kodnest"

    def __init__(self,name,age):
       self.name = name
       self.age = age
    
    def study(self):
        print(f"{self.name} studies")

s1 = Student("ramya",22)
print(f"{s1.name}, {s1.age}, {s1.institute}")
print(Student.institute)
s1.study()

s2 = Student("ramya",22)
print(f"{s2.name}, {s2.age}, {s2.institute}")
s2.study()