# Assignment 9:
# Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().


from abc import ABC ,abstractmethod

class Shape(ABC):
    @abstractmethod
    def display(self):
        pass


class Student(Shape):
    def __init__(self,name):
        self.name = name

    def display(self):
         print(f"My Name is {self.name}")


student1 =Student("Hamza")
print(student1.name)
student1.display()
