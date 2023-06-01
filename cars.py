"""A set of classes that can be used to represent gas and electric cars."""

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


class Battery:
    """A simple attempt to model a battery for an electric car."""
    
    def __init__(self, battery_size):
        """Initialise the battery attributes."""
        self.battery_size = battery_size
        
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
        
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} km on a full charge.")
        
class ElectricCar(Car):
    """Represent aspects of a car specific to electric vehicles."""
    
    def __init__(self, make, model, year, battery_size=75):
        """
        Initialise attributes of the parent class.
        Then initialise attributes specific to an electric car."""
        super().__init__(make, model, year)
        self.battery = Battery(battery_size)
        
    def fill_gas_tank(self):
        """Update method from parent class so we don't put gas in our EV."""
        print("This car doesn't have a gas tank you goof!")