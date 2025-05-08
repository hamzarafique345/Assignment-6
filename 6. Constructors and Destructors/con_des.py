
# Assignment 6:
# Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).

class Logger:
    def __init__(self,val):
        self.val = val
        print("Logger started with value {val}")
    def __del__(self):
        print(f"Logger Destroyed .Last value was {self.val}")

obj1 = Logger(22)
print(obj1.val)
del obj1