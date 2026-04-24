print("----------Method Overriding(Runtime polymorphism)----------")

class Parent:
    def Marry(self):
        print("Marry at the age of 28-30")

class Child(Parent):
    pass
    # def Marry(self):
    #     print("Marry at the age of 30-35")

c = Child()
c.Marry()

class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

d = Dog()
d.sound()
# ex3
class Test:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c

t = Test()

# This will cause a TypeError because Python only remembers the last 'add' method defined
# print(t.add(2, 4)) # Error: missing 1 required positional argument: 'c'

print(t.add(3, 3, 3))
#ex4\
class Test:
    def add(self, *args):
        return sum(args)

t = Test()
print(t.add(2, 4))       # Output: 6
print(t.add(3, 3, 3))    # Output: 9

# + works for nummbers and strings
class Number:
    def __init__(self, value):
        self.value = value #10
    
    def __add__(self, other):
        return self.value + other.value
    
n1 = Number(10)
n2 = Number(20)
print(n1 + n2)

class student:
    def __init__(self, marks):
        self.marks = marks
    
    def __add__(self, other):
        return self.marks + other.marks
    
s1 = student(85)
s2 = student(90)
print(s1+s2)

#duck typing
# Duck Typing and Polymorphism Example

class Dog:
    def speak(self):
        print("Dog barks")

class Cat:
    def speak(self):
        print("Cat meows")

def make_sound(animal):
    animal.speak()

make_sound(Dog())
make_sound(Cat())

# --- Duck Typing with Flying Objects ---

class Parrot:
    def fly(self):
        print("Parrot is flying high in the sky!")

class Airplane:
    def fly(self):
        print("Airplane is taking off!")

# Function using duck typing
def make_it_fly(thing):
    thing.fly()

# Creating instances
parrot = Parrot()
airplane = Airplane()

# Passing different objects to the same function
make_it_fly(parrot)    # Output: Parrot is flying high in the sky!
make_it_fly(airplane)  # Output: Airplane is taking off!