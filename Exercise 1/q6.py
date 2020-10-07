import math


# geometric Shape
class GeometricShape(object):
    def area(self):
        pass

    def perimeter(self):
        pass


# Rectangle
class Rectangle(GeometricShape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * self.height + 2 * self.width


# Square
class Square(Rectangle):
    def __init__(self, side_length):
        Rectangle.__init__(self, side_length, side_length)


# Circle
class Circle(GeometricShape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius


# Triangle
class Triangle(GeometricShape):
    def __init__(self, point1x, point1y, point2x, point2y, point3x, point3y):
        self.point1x = point1x
        self.point1y = point1y

        self.point2x = point2x
        self.point2y = point2y

        self.point3x = point3x
        self.point3y = point3y

    def area(self):
        area = (self.point1x * (self.point2y - self.point3y) + self.point2x* (self.point3y - self.point1y) +
                self.point3x * (self.point1y - self.point2y)) / 2
        return math.fabs(area)

    def perimeter(self):
        length1 = math.sqrt(math.pow((self.point2x - self.point1x), 2) + math.pow((self.point2y - self.point1y), 2))
        length2 = math.sqrt(math.pow((self.point3x - self.point2x), 2) + math.pow((self.point3y - self.point2y), 2))
        length3 = math.sqrt(math.pow((self.point3x - self.point1x), 2) + math.pow((self.point3y - self.point1y), 2))

        perimeter = length1 + length2 + length3
        return perimeter


print("What shape do you want to calculate:")
print("1. Rectangle")
print("2. Square")
print("3. Circle")
print("4. Triangle")
ans = int(input("Answer:"))
if ans == 1:
    hei = float(input("Please enter the Rectangle height: "))
    wid = float(input("Please enter the Rectangle width: "))
    rec = Rectangle(hei, wid)
    print("Rectangle height: %s , width: %s" % (rec.height, rec.width))
    print("Rectangle area: %s" % rec.area())
    print("Rectangle perimeter: %s" % rec.perimeter())
elif ans == 2:
    length = float(input("Please enter the Square length: "))
    sq = Square(length)
    print("Square length: %s , width: %s" % (sq.height, sq.width))
    print("Square area: %s" % sq.area())
    print("Square perimeter: %s" % sq.perimeter())
elif ans == 3:
    rad = float(input("Please enter the Circle radius: "))
    circle = Circle(rad)
    print("Circle radius: %s " % circle.radius)
    print("Circle area: %s" % circle.area())
    print("Circle perimeter: %s" % circle.perimeter())
elif ans == 4:
    p1x = float(input("Please enter the Triangle 1st point (X): "))
    p1y = float(input("Please enter the Triangle 1st point (Y): "))
    p2x = float(input("Please enter the Triangle 2nd point (X): "))
    p2y = float(input("Please enter the Triangle 2nd point (Y): "))
    p3x = float(input("Please enter the Triangle 3rd point (X): "))
    p3y = float(input("Please enter the Triangle 3rd point (Y): "))

    triangle = Triangle(p1x, p1y, p2x, p2y, p3x, p3y)
    print("Triangle area: %s" % triangle.area())
    print("Triangle perimeter: %s" % triangle.perimeter())

else:
    print("You have to choose a number between 1-4 , Bye Bye")
