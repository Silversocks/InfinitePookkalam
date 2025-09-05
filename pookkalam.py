import turtle
import colorsys

# Setup turtle screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Pookkalam Function")

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

# Function to draw a petal
def draw_petal(pen, radius):
    pen.circle(radius, 60)
    pen.left(120)
    pen.circle(radius, 60)
    pen.left(120)

# Function to draw a flower at (x, y) with total_radius
def draw_pookkalam_at(x, y, total_radius, num_layers=2, petals_per_layer=5):
    hue = 0
    layer_thickness = total_radius / num_layers

    for i in range(num_layers):
        current_radius = total_radius - i * layer_thickness

        # Move turtle to start position for layer
        pen.penup()
        pen.goto(x, y)
        pen.setheading(0)
        pen.pendown()

        # Generate color
        hue += 0.12
        rgb = colorsys.hsv_to_rgb(hue % 1, 1, 1)
        color = tuple(int(c * 255) for c in rgb)
        hex_color = '#%02x%02x%02x' % color

        # Draw flower layer
        pen.color(hex_color)
        pen.begin_fill()
        for _ in range(petals_per_layer):
            draw_petal(pen, current_radius / 3)
            pen.right(360 / petals_per_layer)
        pen.end_fill()

# Function to draw a circle around the Pookkalam
def draw_circle_around_pookkalam(x, y, radius):
    pen.penup()
    pen.goto(x, y - radius)  # Move to bottom of the circle
    pen.setheading(0)
    pen.pendown()
    pen.pensize(5)  # Optional: make the outline thicker
    pen.color("black")  # Circle color
    pen.circle(radius)

# Example usage
draw_pookkalam_at(0, 0, 500)
draw_circle_around_pookkalam(0, 0, 180)  # Slightly bigger radius to go around

turtle.done()
