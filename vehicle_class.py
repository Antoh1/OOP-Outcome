class Vehicle(object):
    """A clas for creating various vehicle instances for sale and return their respective selling price"""
    base_sale_price = 0
    wheels = 0
    
    #The constructor for various instance variables
    def __init__(self, miles, make, model):
        self.miles = miles
        self.make = make
        self.model = model
        self.sold_on = None

    def sale_price(self):
        #Return the sale price for this vehicle as a float amount
        if self.sold_on is not None:
            return 'Already sold'
        return 400000.0 * self.wheels

class Car(Vehicle):
    """This class inherits from Vehicle class and create car instance for sale"""

    base_sale_price = 800000
    wheels = 4

class Truck(Vehicle):
    """This class inherits from Vehicle class and create truck instance for sale"""

    base_sale_price = 1000000
    wheels = 8
mak = Car(0,'toyota','corrola')
man = Truck(0,'Man','trailer')    
print(mak.sale_price())
print(man.sale_price())
