class Car:
    """
    Task 1
    - Define a class named Car with attributes: make, model, year
    - Initialize these attributes in the __init__ method
    - Add a method named describe_car() that prints information about the car as "Year Make Model"
    """ 
    # Initialize the attributes
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    # Method to describe the car
    def describe_car(self):
        print(f"{self.year} {self.make} {self.model}")

# Task 2: Creating an instance of the Car class
p1 = Car("Toyota", "Corolla", 2020)

# Calling the describe_car method to print car information
p1.describe_car()
