"""
A class method is a method which is bound to the class and not the object of the class.
-------------------------------------------------------------------------------------
A static method is also a method which is bound to the class and not the object of the class.
A static method can’t access or modify class state.
-----------------------------------------------------------------------------------------
A class method takes cls as first parameter while a static method needs no specific parameters.
A class method can access or modify class state while a static method can’t access or modify it.
"""

# Python program to demonstrate
# use of class method and static method.
from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # a class method to create a Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    # a static method to check if a Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18


person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1996)

print(person1.age)
print(person2.age)

# print the result
print(Person.isAdult(22))
