# Assignment 7:
# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.


class Employee:
    def __init__(self):
        self.name = "Hamza"         # Public variable
        self._salary = 20000        # Protected variable (by convention)
        self.__ssn = "135-32332-32" # Private variable (double underscore)

e = Employee()

# Accessing variables
print(e.name)        # ✅ Works (Public)
print(e._salary)     # ✅ Works (Protected - but accessible)
print(e.__ssn)       # ❌ Error! Private variable
