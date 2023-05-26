from math import pi

class Share:
    def calculate_area(self):
        pass
        
class Rectangle(Share):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def calculate_area(self):
        return self.length*self.width
        
class Circle(Share):
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        return pi*self.radius**2
        
r = Rectangle(5, 3)
c = Circle(2)

print(r.calculate_area())
print(c.calculate_area())