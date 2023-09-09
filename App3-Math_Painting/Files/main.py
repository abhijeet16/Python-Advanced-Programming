from canvas import Canvas
from shapes import Square, Rectangle


# Get canvas width and height from the user
canvas_width = int(input("Enter the width of canvas: "))
canvas_height = int(input("Enter the height of canvas: "))

# Make a dictionary for the colors
colors = {"white": (255, 255, 255), "black": (0, 0, 0)}

# Get the color of canvas as user input
canvas_color = input("Enter the color of canvas (white or black): ")

# Create the canvas with the user choice
canvas = Canvas(height=canvas_height, width=canvas_width, color=colors[canvas_color])

while True:
    shape_type = input("Enter the shape of canvas (Square or Rectangle). Enter quit to quit: ")

    if shape_type.lower() == "rectangle":
        rec_x = int(input("Enter the x coord of rectangle: "))
        rec_y = int(input("Enter the y coord of rectangle: "))
        rec_width = int(input("Enter the width of rectangle: "))
        rec_height = int(input("Enter the height of rectangle: "))
        red = int(input("How much red should the rectangle have? "))
        green = int(input("How much green should the rectangle have? "))
        blue = int(input("How much blue should the rectangle have? "))

        r1 = Rectangle(x=rec_x, y=rec_y, width=rec_width, height=rec_height, color=(red, green, blue))
        r1.draw(canvas)

    if shape_type.lower() == "square":
        sqr_x = int(input("Enter the x coord of square: "))
        sqr_y = int(input("Enter the y coord of square: "))
        sqr_side = int(input("Enter the side of square: "))
        red = int(input("How much red should the square have? "))
        green = int(input("How much green should the square have? "))
        blue = int(input("How much blue should the square have? "))

        r1 = Square(x=sqr_x, y=sqr_y, side=sqr_side, color=(red, green, blue))
        r1.draw(canvas)

    if shape_type == "quit":
        break

canvas.make('canvas.png')
