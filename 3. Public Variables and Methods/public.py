# Assignment 3:
# Create a class Car with a public variable brand and a public method start(). Instantiate the 
# class and access both from outside the class.

class Car:       
    def __init__(self, brandval):
        self.brand = brandval
    
    # method
    def start(self):
        print(f"{self.brand} is Start.")

Car1 = Car("Toyota")
print(Car1.brand)
Car1.start()

