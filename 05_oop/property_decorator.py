# 8. Property Decorators
# Problem: Use a property decorator in the Car class to make the model attribute read-only.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.__model = model  # Private attribute using double underscore

    def full_name(self):
        return f"{self.brand} {self.__model}"

    @property  # The @property decorator allows us to access the method like an attribute
    def model(self):
        return self.__model  # We are returning the private attribute using a getter method

# Creating an instance of the Car class
my_car = Car('BMW', "m5")

print(my_car.brand)   # Accessing public attribute
print(my_car.model)   # Accessing private attribute through the @property getter

# Attempting to change the model directly will throw an error because no setter is defined
my_car.model = 'm8'  # ❌ This will cause an AttributeError

print(my_car.full_name())  # Will still show the original model: BMW m5
