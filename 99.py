class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = None  # Private variable to hold the age
        self.age = age    # Will trigger the setter for age

    @property
    def age(self):
        """Getter for age."""
        return self._age

    @age.setter
    def age(self, value):
        """Setter for age with validation logic."""
        if not isinstance(value, int):
            raise ValueError("Age must be an integer.")
        if value < 0:
            raise ValueError("Age must be a positive number.")
        self._age = value

    @property
    def name(self):
        """Getter for name."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for name with simple validation."""
        if not value or not isinstance(value, str):
            raise ValueError("Name must be a non-empty string.")
        self._name = value


# Example usage:

# Correct usage:
person = Person("Alice", 30)
print(person.name)  # Alice
print(person.age)   # 30

# Trying to set an invalid age:
try:
    person.age = -5  # This will raise a ValueError
except ValueError as e:
    print(e)  # Age must be a positive number.

# Trying to set a non-integer age:
try:
    person.age = "twenty"  # This will raise a ValueError
except ValueError as e:
    print(e)  # Age must be an integer.

# Trying to set an invalid name:
try:
    person.name = ""  # This will raise a ValueError
except ValueError as e:
    print(e)  # Name must be a non-empty string.
