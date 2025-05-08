# Assignment 13:
# Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization.
# Access a method of the Engine class via the Car class.


class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self):
        self.engine = Engine()  

    def start_car(self):
        return self.engine.start()  
my_car = Car()
print(my_car.start_car()) 
