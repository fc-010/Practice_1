class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height

    def __str__(self):
        return f"Rectangle({self.width} x {self.height})"


R1 = Rectangle(4, 6)
R2 = Rectangle(5, 5)

print(R1, R1.area(), R1.perimeter(), R1.is_square())
print(R2.is_square())
