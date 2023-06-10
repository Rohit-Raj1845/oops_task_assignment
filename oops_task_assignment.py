QUESTION:-1. Create a vehicle class with an init method having instance variables as name_of_vehicle, max_speed and average_of_vehicle.
class vehicle : 
    def __init__(self , name_of_vehicle , max_speed , average_of_vehicle): 
        self.__name_of_vehicle = name_of_vehicle
        self.__max_speed = max_speed
        self.__average_of_vehicle = average_of_vehicle
        
class Bus(vehicle):
    pass

c = vehicle("Bus" , 180 , 20)
print(c._vehicle__name_of_vehicle)
print(c._vehicle__max_speed)
print(c._vehicle__average_of_vehicle)



QUESTION:-2. Create a child class car from the vehicle class created in Que 1,which will inherit the vehicle class. Create a method named seating_capacity which takes capacity as an argument and returns the name of the vehicle and its seating capacity.
class vehicle : 
    def __init__(self , name_of_vehicle , seating_capacity): 
        self.name_of_vehicle = name_of_vehicle
        self.seating_capacity = seating_capacity
        
    def child_class_car(self): 
        return self.name_of_vehicle , self.seating_capacity
child = vehicle("Car" , 4)     
print(child.child_class_car())  



QUESTION:-3. What is multiple inheritance? Write a python code to demonstrate multiple inheritance.
Multiple inheritance is a feature of some object-oriented computer programming languages in which an object or class can inherit features from more than one parent object or parent class.

class Class1: 

    def m(self): 
        print("In Class1")

class Class2(Class1): 

    def m(self): 
        print("In Class2")

class Class3(Class1): 

    def m(self): 
        print("In Class3")

class Class4(Class2 , Class3): 
    pass

obj = Class4()
obj.m()



QUESTION:-4. What are getter and setter in python? Create a class and create a getter and a setter method in this class.
Getter:- A method that allows you to access an attribute in a given class.
Setter:- A method that allows you to set or mutate the value of an attribute in a class.

class Greek: 

    def __init__(self, age = 0): 
        self._age = age

    def get_age(self): 
        return self._age 

    def set_age(self, x): 
        self._age = x

raj = Greek()
raj.set_age(21)
print(raj.get_age())
print(raj._age)           



QUESTION:-5. What is method overriding in python? Write a python code to demonstrate method overriding.
Method overriding is a feature of object-oriented programming languages where the subclass or child class can provide the program with specific characteristics or a specific implementation process of data provided that are already defined in the parent class or superclass.
class Parent(): 

    def __init__(self): 
        self.value = "Inside Parent"

    def show(self): 
        print(self.value)

class Child(Parent): 

    def __init__(self): 
        self.value = "Inside Child" 

    def show(self): 
        print(self.value)

obj1 = Parent()
obj2 = Child()

obj1.show()
obj2.show()
