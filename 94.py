class Circle:
    def draw(self):
        print("Drawing a Circle")

class Triangle:
    def draw(self):
        print("Drawing a Triangle")

# Example usage
shapes = [Circle(), Triangle()]
for shape in shapes:
    shape.draw()
