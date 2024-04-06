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
def draw_heart():
    t.goto(0,-100)
    t.pendown()
    t.begin_fill()
    t.left(140)
    t.forward(224)
    for i in range(200):
        t.right(1)
        t.forward(2 )
    t.left(120)
    for i in range(200):
        t.right(1)
        t.forward(2)
    t.forward(224)
    t.end_fill()
    t.penup()

# Draw heart shape
draw_heart()

# Write the birthday message inside the heart
t.goto(0,90)
t.color("white")
t.write("HAPPY BIRTHDAY BRO", align="center", font=("Monotype Corsiva", 24, "bold"))

# Hide the turtle
t.hideturtle()

# Close the turtle graphics window on click
screen.exitonclick()
