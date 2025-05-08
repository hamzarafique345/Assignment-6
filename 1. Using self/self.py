# Assignment 1:
# Create a class Student with attributes name and marks. Use the self keyword to initialize these values 
# via a constructor. Add a method display() that prints student details.


class Student:     #{}
      def __init__(self ,name1 , marks1):
            #key        value
            self.name = name1
            self.marks = marks1
      
      # method
      def Display(self):
            print(f"My name is {self.name} and my salary is {self.marks}")


student1 =Student("Hamza" , 1200 )
print(student1.name)
student1.Display()

student2 =Student("Ali" , 1300)
student2.Display()
