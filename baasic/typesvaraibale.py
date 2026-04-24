#public members-procted-
class Person:
    def __init__(self,name):
        self.name = name #public

p = Person("ramya")
print(p.name)
##procted
# Public members - Protected _ - 

class Person:
    def __init__(self, name):
        self._name = name # protected

class student(Person):
    def display(self):
        print(self._name)

p = student("Gamana")
p.display()
print(p._name)

#private 
class Employee:
    # Constructor (assumed based on usage)
    def __init__(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, amt):
        if amt >= 0:
            self.__salary = amt

e = Employee(30000)
print(e.get_salary())
e.set_salary(50000)
print(e.get_salary())
# print(e.__salary) Error
# Name Mangling
print()