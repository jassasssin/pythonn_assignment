class Car:
    def __init__(self, make="Unknown", model="Unknown", year=0):
        self.make = make
        self.model = model
        self.year = year

# Example usage
car = Car()
print(f"Car: {car.make} {car.model}, Year: {car.year}")
