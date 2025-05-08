# Assignment 10:
# Create a class Dog with instance variables name and breed. Add an instance method bark() that prints a message including the dog's name.

class Dog:
    def __init__(self,name ,bread):
        self.name = name 
        self.bread = bread

    def bark(self):
        print(f"{self.name} is barking")

obj1 = Dog("Tommy","Down")
print(obj1.name)
obj1.bark()