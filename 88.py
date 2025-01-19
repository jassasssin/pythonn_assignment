class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

# Example usage
car = Car("Toyota", "Corolla", 2020)
print(f"Car: {car.make} {car.model}, Year: {car.year}")
