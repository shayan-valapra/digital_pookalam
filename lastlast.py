import turtle 
import time
import math

# Setup
t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("white")
t.speed(0)
turtle.colormode(255)

# Function to draw a petal
def petal(t, radius, angle, color):
    t.fillcolor(color)
    t.pencolor(color)  # Outline matches fill color
    t.begin_fill()
    t.circle(radius, angle)
    t.left(180 - angle)
    t.circle(radius, angle)
    t.left(180 - angle)
    t.end_fill()

# Function to draw a tiny flower at current position
def tiny_flower(t, radius=10, petals=5, color=(255, 255, 255)):
    t.fillcolor(color)
    t.pencolor(color)
    t.begin_fill()
    for _ in range(petals):
        t.circle(radius, 60)
        t.left(180 - 60)
        t.circle(radius, 60)
        t.left(180 - 360/petals)
    t.end_fill()

# Traditional Kerala flower-inspired colors for petals
colors = [
    (255, 215, 0),    # Yellow - innermost layer
    (255, 140, 0),    # Orange
    (255, 0, 0),      # Red
    (255, 255, 255)   # White - outermost layer
]

# Parameters
num_layers = 4
max_radius = 220       # outermost petal radius
max_angle = 90         # outermost petal angle

# Compute circle radius exactly matching petal tip, then decrease slightly
circle_radius = 2 * max_radius * math.sin(math.radians(max_angle/2)) - 30

# Draw outer dark green circle first
outer_circle_radius = circle_radius + 60
t.penup()
t.goto(0, -outer_circle_radius)
t.pendown()
t.fillcolor((0, 100, 0))
t.pencolor((0, 100, 0))
t.begin_fill()
t.circle(outer_circle_radius)
t.end_fill()

# Fill central red circle
t.penup()
t.goto(0, -circle_radius + 2)
t.pendown()
t.fillcolor((255, 0, 0))
t.pencolor((255, 0, 0))
t.begin_fill()
t.circle(circle_radius - 2)
t.end_fill()

# Draw red circle boundary
t.penup()
t.goto(0, -circle_radius)
t.pendown()
t.pensize(3)
t.color((255, 0, 0))
t.circle(circle_radius)
t.pensize(1)
t.color("black")

# Animate petals from innermost to outermost
for layer in range(num_layers):
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.setheading(layer * 15)
    petals = 8 + layer * 3
    radius = max_radius - layer * 50
    angle = max_angle - layer * 5
    
    color = colors[layer % len(colors)]
    
    for _ in range(petals):
        petal(t, radius, angle, color)
        t.right(360 / petals)
        time.sleep(0.05)

# Draw white flowers at tips of innermost petals
t.penup()
t.goto(0, 0)
t.setheading(0)
innermost_petals = 8
innermost_radius = max_radius
innermost_angle = max_angle

for i in range(innermost_petals):
    t.penup()
    t.setheading(i * (360 / innermost_petals))
    tip_distance = 2 * innermost_radius * math.sin(math.radians(innermost_angle/2))
    t.forward(tip_distance)
    t.pendown()
    tiny_flower(t, radius=10, petals=5, color=(255, 255, 255))  # White
    t.penup()
    t.goto(0, 0)

# Draw yellow flowers at tips of outermost petals
outermost_layer = num_layers - 1
outermost_petals = 8 + outermost_layer * 3
outermost_radius = max_radius - outermost_layer * 50
outermost_angle = max_angle - outermost_layer * 5

for i in range(outermost_petals):
    t.penup()
    t.setheading(i * (360 / outermost_petals))
    tip_distance = 2 * outermost_radius * math.sin(math.radians(outermost_angle/2))
    t.forward(tip_distance)
    t.pendown()
    tiny_flower(t, radius=10, petals=5, color=(255, 215, 0))  # Yellow
    t.penup()
    t.goto(0, 0)

# Function to write text along the circle
def write_text_circle_animated(t, text, radius, spacing=20):
    circumference = 2 * math.pi * radius
    total_angle = 360 * (spacing * len(text)) / circumference
    start_angle = 90 + total_angle / 2
    t.penup()
    t.goto(0, 0)
    t.setheading(start_angle)
    t.forward(radius)
    t.pencolor("red")
    for char in text:
        t.setheading(t.towards(0,0) + 90)
        t.pendown()
        t.write(char, align="center", font=("Arial", 18, "bold"))
        t.penup()
        t.backward(-spacing)
        t.right(spacing / circumference * 360)
        time.sleep(0.1)

# Add animated circular text
write_text_circle_animated(t, "HAPPY ONAM TINKERHUB GECK", radius=circle_radius + 70, spacing=30)

t.hideturtle()
turtle.done()
