import math

# main class
class Shape:
    def __init__(self):
        pass
    
    def area(self):
        pass
    
    def perimeter(self):
        pass

# child classes
# circle class

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = math.pi * (self.radius ** 2)
        return area

    def perimeter(self):
        perimeter = 2 * math.pi * self.radius
        return perimeter

# rectangle class

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        area =  self.width * self.height
        return area

    def perimeter(self):
        perimeter =  2 * (self.width + self.height)
        return perimeter

# triangle class

class Triangle(Shape):
    def __init__(self, a, b, c):
        # sides of the triangle
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        # herons formula
        s = (self.a + self.b + self.c) / 2
        if (self.a + self.b) <= self.c or (self.c + self.b) <= self.a or (self.a + self.c) <= self.b:
            area = "invalid data"
        else:
            area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return area

    def perimeter(self):
        perimeter = self.a + self.b + self.c
        return perimeter



# circle

circle = Circle(1)
print("Circle:")
print(f"Radius: {circle.radius}")
print(f"Area: {circle.area():.2f}")
print(f"Perimeter: {circle.perimeter():.2f}")
print()

# rectangle

rectangle = Rectangle(4, 16)
print("Rectangle:")
print(f"Width: {rectangle.width}, Height: {rectangle.height}")
print(f"Area: {rectangle.area()}")
print(f"Perimeter: {rectangle.perimeter()}")
print()

# invalid triangle

triangle = Triangle(3, 8, 5)
print("Triangle:")
print(f"Sides: {triangle.a}, {triangle.b}, {triangle.c}")
print(f"Area: {triangle.area():}")
print(f"Perimeter: {triangle.perimeter()}")
print()

# valid triangle

triangle = Triangle(3, 5, 5)
print("Triangle:")
print(f"Sides: {triangle.a}, {triangle.b}, {triangle.c}")
print(f"Area: {triangle.area():}")
print(f"Perimeter: {triangle.perimeter()}")



