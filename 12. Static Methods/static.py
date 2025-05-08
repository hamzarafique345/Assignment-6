# Assignment 12:
# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.



class TempertatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

Celcius1 = TempertatureConverter.celsius_to_fahrenheit(100)
print(Celcius1)
        