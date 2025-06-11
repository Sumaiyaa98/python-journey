# 7. Static Method
# Problem: Add a static method to the Car class that returns a general description of a car.

class Car:
   
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        
    
    def fullName(self):
        return f"{self.brand}{self.model}"
    
    @staticmethod
    def general_description():
        return "Cars are means of transport"

my_car = Car("BMW","m4")
print(my_car.fullName())
print(my_car.general_description())
print(Car.general_description())


# ✅ What is a @staticmethod?
# A @staticmethod in Python is a method inside a class that:

# Does NOT take self or cls as its first parameter.

# Does not depend on instance variables or class variables.

# Can be called with or without creating an object of the class.

# 🔍 Why use @staticmethod?
# To define a function inside a class that is logically related to the class...

# ...but does not need to access the class (cls) or the instance (self).

# 🧪 Example:

class MathTools:
    @staticmethod
    def add(x, y):
        return x + y
# You can call it either way:


print(MathTools.add(3, 5))  # ✅ Called without object
tool = MathTools()
print(tool.add(3, 5))       # ✅ Al