# 10. Multiple Inheritance
# Problem: Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.

class Battery:
    def battery_info(self):
        return "this is battery"


class Engine:
     def engine_info(self):
        return "this is engine"

class ElectricCar(Battery,Engine):
    pass

my_electric_car = ElectricCar()
print(my_electric_car.battery_info())
print(my_electric_car.engine_info())

