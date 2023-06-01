"""A class that can be used to represent a car."""

class Car:
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """Initialize attrbiutes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's kms."""
        print(f"This car has {self.odometer_reading} km on it.")
        
    def update_odometer(self, kms):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back
        """
        if kms >= self.odometer_reading:
            self.odometer_reading = kms
        else:
            print("You can't roll the odometer back you crook!")
            
    def increment_odometer(self, kms):
        """Add the given amount to the odometer reading."""
        if kms >= 0:
            self.odometer_reading += kms
        else:
            print("You can't roll the odometer back you crook!")
            
    def fill_gas_tank(self):
        """Fill up that tank"""
        print("Excellent stuff that's exactly what you should do with your car!")