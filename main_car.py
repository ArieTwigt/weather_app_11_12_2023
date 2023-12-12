
# parent class
class Vehicle:

    # inital attributes
    def __init__(self, brand, color, price=0):
        self.brand = brand
        self.color = color
        self.price = price

    # method to change the price
    def change_price(self, price_change):
        # check if the price will not be negative
        if self.price + price_change < 0:
            raise ValueError("Price change cannot be higher than current price")
        
        print(f"Old price: {self.price}")
        self.price += price_change
        print(f"New price: {self.price}")


    # how to represent the object
    def __repr__(self):
        return f"{self.brand}-{self.color}-{self.price}"
    

# define the Car class
class Car(Vehicle):
    wheels = 4


class MotorCycle(Vehicle):
    wheels = 2

    # how to represent the object
    def __repr__(self):
        return f"{self.color}-{self.price}-{self.brand}"


if __name__ == "__main__":
    # initate a Car instance
    my_car = Car("Audi", "red", 1000)
    my_motor_cycle = MotorCycle("Kawasaki", "Red", 5000)
    pass

