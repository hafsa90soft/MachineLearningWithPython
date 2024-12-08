import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(5)
t.pensize(3)
t.color("#FF1493")  # Hot pink color for main text

def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# Draw decorative header line
def draw_header():
    t.color("#9932CC")  # Purple color for decorative elements
    move(-300, 100)
    t.forward(600)
    
    # Add small decorative elements along the line
    for x in range(-300, 301, 60):
        move(x, 100)
        t.right(90)
        t.forward(10)
        t.backward(20)
        t.forward(10)
        t.left(90)

# Draw decorative footer line
def draw_footer():
    t.color("#9932CC")
    move(-300, -50)
    t.forward(600)
    
    # Add small decorative elements along the line
    for x in range(-300, 301, 60):
        move(x, -50)
        t.right(90)
        t.forward(10)
        t.backward(20)
        t.forward(10)
        t.left(90)

# Draw the letter H
def draw_h(x):
    move(x, 50)
    t.color("#FF1493")
    t.left(90)
    t.forward(80)
    t.backward(40)
    t.right(90)
    t.forward(40)
    t.left(90)
    t.forward(40)
    t.backward(80)
    t.right(90)
    
    # Decorative element
    move(x+20, 90)
    t.circle(5)

# Draw the letter A
def draw_a(x):
    move(x, 50)
    t.color("#FF1493")
    t.left(75)
    t.forward(85)
    t.right(150)
    t.forward(85)
    t.backward(40)
    t.right(105)
    t.forward(30)
    
    # Decorative element
    move(x+20, 90)
    t.circle(5)

# Draw the letter F
def draw_f(x):
    move(x, 50)
    t.color("#FF1493")
    t.left(90)
    t.forward(80)
    t.right(90)
    t.forward(40)
    t.backward(40)
    t.right(90)
    t.forward(40)
    t.left(90)
    t.forward(30)
    t.backward(30)
    t.right(90)
    t.forward(40)
    t.left(90)
    
    # Decorative element
    move(x+20, 90)
    t.circle(5)

# Draw the letter S
def draw_s(x):
    move(x, 50)
    t.color("#FF1493")
    t.forward(40)
    t.backward(40)
    t.left(90)
    t.forward(40)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(40)
    t.left(90)
    
    # Decorative element
    move(x+20, 90)
    t.circle(5)

# Draw decorative separator
def draw_separator(x):
    move(x, 50)
    t.color("#9932CC")
    t.left(90)
    for _ in range(3):
        t.forward(5)
        t.backward(5)
        t.right(120)
    t.right(90)

# Draw header
draw_header()

# Starting position
start_x = -250

# Draw each letter with separators
draw_h(start_x)
draw_separator(start_x + 60)
draw_a(start_x + 100)
draw_separator(start_x + 160)
draw_f(start_x + 200)
draw_separator(start_x + 260)
draw_s(start_x + 300)
draw_separator(start_x + 360)
draw_a(start_x + 400)

# Draw footer
draw_footer()

# Add final decorative elements
def draw_corner_decoration(x, y):
    move(x, y)
    t.color("#9932CC")
    for _ in range(4):
        t.circle(10, 90)
        t.forward(10)

# Add corner decorations
corners = [(-300, 100), (300, 100), (-300, -50), (300, -50)]
for x, y in corners:
    draw_corner_decoration(x, y)

# Hide turtle and complete
t.hideturtle()
turtle.done()






