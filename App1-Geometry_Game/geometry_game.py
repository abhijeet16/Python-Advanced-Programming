# import libraries
from random import randint
import turtle

# Create the class Point
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        lowerx = min(rectangle.point1.x, rectangle.point2.x)
        upperx = max(rectangle.point1.x, rectangle.point2.x)
        lowery = min(rectangle.point1.y, rectangle.point2.y)
        uppery = max(rectangle.point1.y, rectangle.point2.y)

        if lowerx < self.x < upperx \
            and lowery < self.y < uppery:
            return True
        else:
            return False


# Create the class Rectangle
class Rectangle:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return abs((self.point2.x - self.point1.x) * (self.point2.y - self.point1.y))
    

# create the GUI rectangle class
class GuiRectangle(Rectangle):
    def draw(self, canvas):
        # Go to point 1
        canvas.penup()
        canvas.goto(self.point1.x, self.point1.y)
        canvas.pendown()

        # Draw Rectangle
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90) # Turn 90 degrees
        canvas.forward(self.point2.y - self.point1.y)
        canvas.left(90) # Turn 90 degrees
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90) # Turn 90 degrees
        canvas.forward(self.point2.y - self.point1.y)


# create the GUI point class
class GuiPoint(Point):
    def draw(self, canvas, size=10, color='red'):

        # Draw point
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)

        turtle.done()


# Create an instance/object of rectangle class with random coordinates
rectangle = GuiRectangle(
    Point(randint(0,200), randint(0,200)),
    Point(randint(200,400), randint(200,400))
    )

# Print rectangle canvas
print(f"Rectangle Coordinates: {rectangle.point1.x, rectangle.point1.y} and {rectangle.point2.x, rectangle.point2.y}")

# Get the point and area from the user
user_point = GuiPoint(float(input("Guess X: ")), float(input("Guess Y: ")))
user_area = float(input("Guess rectangle area: "))

# Check if the instance point falls in the given rectangle
print("Your point lies in the rectangle: ", user_point.falls_in_rectangle(rectangle))

# Print difference of areas
print("Your area is off by:", abs(rectangle.area() - user_area))

# Create an instance of turtle class
myTurtle = turtle.Turtle()

# Draw on canvas
rectangle.draw(canvas=myTurtle)
user_point.draw(canvas=myTurtle)
