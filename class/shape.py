class Shape:
    def info(self):
        print("It is a n dimensional shape")

class Rectangle(Shape):
    def area(self):
        print("It is an area of the Rectangle")


obj1= Rectangle()

obj1.info()
obj1.area()

# Multiple Inheritance
class Area:
    def calculate(self, area):
        return area
    
class length:
    def calculateLength(self, length):
        return length

class Cube(Area, length):
    def volume(self, area, length):
        return area * length
    
obj1 = Cube()
a = obj1.calculate(4)
b = obj1.calculateLength(3)
c = obj1.volume(5,6)

print("Area: ", a)
print("Length: ", b)
print("Volume: ", c)

class Area:
    def print_area(self):
        a = self.length * self.breadth
        print("Area is: ", a)
 

class Perimeter:
    def peri(self):
        b = 2 * (self.length+ self.breadth)
        print("The perimeter is", b)

class Rectangle(Area, Perimeter):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        
objn = Rectangle(4, 6)
obj2 = Area()
obj3 = Perimeter()

objn.print_area()
objn.peri()