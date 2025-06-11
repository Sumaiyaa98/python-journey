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