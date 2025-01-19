class Circle:
    def draw(self):
        print("Drawing a Circle")

class Square:
    def draw(self):
        print("Drawing a Square")

class Triangle:
    def draw(self):
        print("Drawing a Triangle")

# Example usage
shapes = [Circle(), Square(), Triangle()]
for shape in shapes:
    shape.draw()
