class rectangle:
    length=0
    breadth=0
    def area(self):
        a = self.length* self.breadth
        print("Area of rectangle is", a)

obj1 = rectangle()
obj1.length = 20
obj1.breadth = 10
obj1.area()


class circle:
    def __init__(self, radius):
        self.radius = radius
    def circumference(self):
        print("Circumference=",2*3.14*self.radius)
    def area(self):
        print("Area=",3.14*self.radius*self.radius)

obj2 = circle(8)
obj2.circumference()
obj2.area()
