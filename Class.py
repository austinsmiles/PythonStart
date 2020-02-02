class Person:
    def __init__(self, name, age):  # first param of init() is the instance reference, doesnt have to be self
        self.name = name
        self.age = age

    def greet(self):
        print("Hello my name is " + self.name)


p1 = Person("John", 36)
p1.greet()


class Student(Person):  # Inheriting the Person parent class into the Student child class
    pass
