import turtle

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("lightblue")

# Create a turtle
t = turtle.Turtle()
t.speed(0)
t.color("red")
t.penup()

# Function to draw a heart
def draw_heart(x, y, size):
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.left(140)
    t.forward(120 * size)
    for i in range(200):
        t.right(1)
        t.forward(2 * size)
    t.left(120)
    for i in range(200):
        t.right(1)
        t.forward(2 * size)
    t.forward(120 * size)
    t.end_fill()
    t.penup()

# Draw heart shape
draw_heart(0, 0, 1)

# Write the birthday message inside the heart
t.goto(0, -30)
t.color("white")
t.write("Happy Birthday Bro", align="center", font=("Arial", 20, "normal"))

# Hide the turtle
t.hideturtle()

# Keep the window open
screen.mainloop()
