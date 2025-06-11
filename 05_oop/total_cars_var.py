# 6. Class Variables
# Problem: Add a class variable to Car that keeps track of the number of cars created.
  
class Car:
    total_car = 0

    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        Car.total_car += 1 #another way to call attribut
    
    def fullName(self):
        return f"{self.brand}{self.model}"

my_car = Car("BMW","m4")
print(my_car.fullName())
print(Car.total_car)
    
