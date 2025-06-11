# 9. Class Inheritance and isinstance() Function
# Problem: Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar.

class Car:
   
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model

    def full_name(self):
        return f"{self.__brand} {self.__model}"

class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)
        #super is used to inherit the method from our main class, we also have
        #to pass the attribute as well
        self.batter_size = battery_size
    
   

tesla_car = ElectricCar("Tesla","Model S","84kWh")
print(tesla_car.full_name())
print(isinstance(tesla_car,Car))
print(isinstance(tesla_car,ElectricCar))

#isinstance is a builtin method to check that any specific object is an instnce of any specific class or not,
#for this we have to pass two values, first the object name, second class name