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

# 2. Class Method and Self
# Problem: Add a method to the Car class that displays the full name of the car (brand and model).
    def full_name(self):
        return f"{self.brand} {self.model}"


# Create an object (instance) of the Car class with brand "BMW" and model "m4"
car_01 = Car("BMW", "m4")

# Access the attributes of the object using dot notation
print(car_01.brand)  # Output: BMW
print(car_01.model)  # Output: m4
print(car_01.full_name())


# 3. Inheritance
# Problem: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.

class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)
        #super is used to inherit the method from our main class, we also have
        #to pass the attribute as well
        self.batter_size = battery_size

my_electric_car = ElectricCar("Tesla","Model S","84kWh")
print(my_electric_car.brand)
print(my_electric_car.batter_size)
print(my_electric_car.full_name())



# 4. Encapsulation
# Problem: Make the Person class to encapsulate the age attribute, making it private, and provide a getter method for it.
class Person:
    def __init__(self,name,age):
        self.name = name
        self.__age = age
        #'__' used to make private attribute that can only access by using getter method for users
    
    def get__age(self):
        return f"{self.__age}"

person_01 = Person("Alex",29)
print(person_01.name)
print(person_01.get__age())

    
    
