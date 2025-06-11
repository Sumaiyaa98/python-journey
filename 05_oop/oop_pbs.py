# 1. Basic Class and Object
# Problem: Create a Car class with attributes like brand and model. Then create an instance of this class.

# Define a class called 'Car'
class Car:
    # __init__ is a special method that runs automatically when we create an object from the class
    # It is used to initialize (set) the values of the object's properties
    def __init__(self, brand, model):
        # 'self' refers to the current object being created
        # We use 'self' to attach the passed values to the object
        self.brand = brand    # set the object's 'brand' attribute
        self.model = model    # set the object's 'model' attribute

# Create an object (instance) of the Car class with brand "BMW" and model "m4"
car_01 = Car("BMW", "m4")

# Access the attributes of the object using dot notation
print(car_01.brand)  # Output: BMW
print(car_01.model)  # Output: m4
