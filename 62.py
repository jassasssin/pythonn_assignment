class Animal:
    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")

class Dog(Animal):
    def speak(self):
        print("Woof!")

# Example usage
dog = Dog()
dog.speak()
