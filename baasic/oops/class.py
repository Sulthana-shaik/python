class Student:
    def __init__(self, name, age, institute):
        self.name = name
        self.age = age
        self.institute = institute
    def study(self):
        print(f"{self.name} Studies")

s1 = Student("Abhi", 21, "Kodnest")
print(f"{s1.name}, {s1.age}, {s1.institute}")
s1.study()

s2 = Student("Viju", 22, "Kodnest")
print(f"{s2.name}, {s2.age}, {s2.institute}")
s2.study()