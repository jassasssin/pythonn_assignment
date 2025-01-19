class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

# Example usage
square = Square(5)
print(f"Square Length: {square.length}, Width: {square.width}")
