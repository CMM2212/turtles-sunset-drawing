#############################################
# Name: Colin McLean
# Submission Date: 9/20/2022
# Minnesota State University Moorhead
# Class: CSIS 152
# Assignment 07
#############################################
import turtle
import time

# Create the turtle window and turtle instance
window = turtle.Screen()
window.setup(1084, 570)
alex = turtle.Turtle()

time.sleep(4)
turtle.colormode(255)
alex.speed(0)

# Set some constants for the general shape/size of things.
frame_width = 1080
frame_height = 566
frame_thickness = 25
sky_height = 325
ocean_height = frame_height - sky_height
gradient_thickness = 5
sun_origin = frame_height // 2 - sky_height
sun_radius = 100
sun_reflection_length = 190


# Draw Frame
alex.pensize(frame_thickness)
alex.forward(frame_width / 2)
alex.left(90)
alex.forward(frame_height / 2)
alex.left(90)
alex.forward(frame_width)
alex.left(90)
alex.forward(frame_height)
alex.left(90)
alex.forward(frame_width)
alex.left(90)
alex.forward(frame_height - 5)
alex.left(90)

# Draw sky
alex.pensize(gradient_thickness)
initial_red = 228
initial_green = 3
initial_blue = 109
target_red = 250
target_green = 139
target_blue = 83

# Calculate the color steps required to create a smooth gradient effect
red_step = (target_red - initial_red) / (sky_height // gradient_thickness)
green_step = (target_green - initial_green) / (sky_height // gradient_thickness)
blue_step = (target_blue - initial_blue) / (sky_height // gradient_thickness)

red = initial_red
green = initial_green
blue = initial_blue

next_angle = 90
for i in range(sky_height // gradient_thickness):
    red += red_step
    green += green_step
    blue += blue_step
    next_angle = (next_angle + 180) % 360
    alex.pencolor(int(red), int(green), int(blue))
    alex.forward(frame_width)
    alex.right(next_angle)
    alex.forward(gradient_thickness)
    alex.right(next_angle)

# Draw Sun
initial_red = 246
initial_green = 155
initial_blue = 67
target_red = 250
target_green = 234
target_blue = 0

red_step = (target_red - initial_red) / (sun_radius // gradient_thickness)
green_step = (target_green - initial_green) / (sun_radius // gradient_thickness)
blue_step = (target_blue - initial_blue) / (sun_radius // gradient_thickness)

red = initial_red
green = initial_green
blue = initial_blue

sun_top = sun_origin + sun_radius
alex.pensize(gradient_thickness + 2)
alex.setheading(180)
for i in range(sun_radius // gradient_thickness):
    alex.penup()
    alex.goto(0, sun_top)
    alex.pendown()
    red += red_step
    green += green_step
    blue += blue_step
    alex.pencolor(int(red), int(green), int(blue))
    alex.circle(sun_radius - i * gradient_thickness)
    sun_top -= gradient_thickness


# Draw Ocean
initial_red = 51
initial_green = 73
initial_blue = 117
target_red = 123
target_green = 99
target_blue = 126

red_step = (target_red - initial_red) / (ocean_height // gradient_thickness)
green_step = (target_green - initial_green) / (ocean_height // gradient_thickness)
blue_step = (target_blue - initial_blue) / (ocean_height // gradient_thickness)

red = initial_red
green = initial_green
blue = initial_blue

alex.penup()
alex.goto(frame_width // 2, frame_height // 2 - sky_height)
alex.pendown()
next_angle = 90

for i in range(ocean_height // gradient_thickness):
    red += red_step
    green += green_step
    blue += blue_step
    next_angle = (next_angle + 180) % 360
    alex.pencolor(int(red), int(green), int(blue))
    alex.forward(frame_width)
    alex.right(next_angle)
    alex.forward(gradient_thickness)
    alex.right(next_angle)

# Draw Sun Reflection
initial_red = 133
initial_green = 155
initial_blue = 200
target_red = 191
target_green = 123
target_blue = 136

red_step = (target_red - initial_red) / (sun_reflection_length // gradient_thickness)
green_step = (target_green - initial_green) / (sun_reflection_length // gradient_thickness)
blue_step = (target_blue - initial_blue) / (sun_reflection_length // gradient_thickness)

red = initial_red
green = initial_green
blue = initial_blue
alex.penup()
alex.goto(sun_radius, sun_origin)
alex.pendown()
alex.setheading(180)
reflection_width = sun_radius * 2
for i in range(sun_reflection_length // gradient_thickness):
    red += red_step
    green += green_step
    blue += blue_step
    next_angle = (next_angle + 180) % 360
    alex.pencolor(int(red), int(green), int(blue))
    alex.forward(reflection_width)
    alex.right(next_angle)
    alex.forward(gradient_thickness)
    alex.right(next_angle)
    reflection_width -= (2 + i//5)

alex.setheading(0)
alex.penup()
alex.setposition(-250, -160)
alex.pendown()
alex.pencolor("black")

# Boat Body
alex.begin_fill()
alex.left(180)
alex.forward(175)
alex.right(64)
alex.forward(40)
alex.right(116)
alex.forward(194)
alex.right(90)
alex.forward(36)
alex.end_fill()

# Boat Front
alex.pensize(2)
alex.left(135)
alex.forward(51)
alex.left(135)
alex.pensize(4)
alex.forward(120)
alex.pensize(1)
alex.forward(105)

# Boat Flag
alex.forward(4)

alex.begin_fill()
alex.pensize(3)
alex.right(60)
alex.forward(20)
alex.left(135)
alex.forward(15)
alex.left(135)
alex.forward(12)
alex.end_fill()

alex.right(90)
alex.forward(10)
alex.left(60)
alex.forward(4)
alex.right(180)

# Boat Back Sail
alex.pensize(2)
alex.right(120)
alex.forward(36)
alex.left(115)
alex.pensize(4)
alex.forward(10)
alex.left(180)
alex.forward(10)
alex.begin_fill()
alex.forward(105)
alex.left(90)
alex.forward(205)
alex.left(154)
alex.forward(225)


alex.pensize(2)
alex.left(115)
alex.forward(95)
alex.right(75)
alex.forward(50)
alex.left(90)
alex.forward(10)
alex.left(80)
alex.forward(220)
alex.end_fill()

# Boat Center Pole
alex.pensize(6)
alex.right(180)
alex.forward(160)
alex.left(176)
alex.forward(175)
alex.right(180)
alex.forward(10)

# Boat Front Sail
alex.pensize(2)
alex.left(17)
alex.forward(40)

alex.begin_fill()
alex.left(9)
alex.forward(150)
alex.right(115)
alex.forward(65)
alex.end_fill()

alex.pensize(4)
alex.left(70)
alex.forward(30)
alex.right(180)
alex.forward(30)
alex.right(70)
alex.forward(65)

alex.pensize(3)
alex.right(54)
alex.forward(24)

# Boat Shadow

alex.pencolor(24, 32, 45)
alex.fillcolor(24, 32, 45)
alex.setheading(0)
alex.penup()
alex.setposition(-250, -162 )
alex.pendown()
alex.begin_fill()
alex.right(135)
alex.forward(150)
alex.right(45)
alex.forward(175)
alex.right(135)
alex.forward(150)
alex.end_fill()


# Draw Birds
alex.penup()
alex.goto(140, 150)
alex.pendown()

alex.setheading(0)
alex.pencolor("black")
alex.pensize(1)
for i in range(3):
    for j in range(5 -i):
        alex.penup()
        alex.setposition(200 + i*20 + j*40 + j%2*6, -20 + i * 20 + (j + i)%3*3 + (j + i)%2*2)
        alex.setheading(0)
        alex.pendown()
        alex.left(90)
        for k in range(2):
            for l in range(18 - (i*3)):
                alex.right(180 / (18 - i*3))
                alex.forward(1)
            alex.left(180)
    
# Draw base of lighthouse
alex.pensize(1)
y_base = -frame_height // 2 + frame_thickness // 2
square_height = 320
square_width = 75
shaded_width = 50
initial_red = 99
initial_green = 29
initial_blue = 46
target_red = 0
target_green = 0
target_blue = 0

red_step = (target_red - initial_red) / (shaded_width // gradient_thickness)
green_step = (target_green - initial_green) / (shaded_width // gradient_thickness)
blue_step = (target_blue - initial_blue) / (shaded_width // gradient_thickness)

red = initial_red
green = initial_green
blue = initial_blue

alex.penup()
alex.setheading(90)
alex.setposition(frame_width // 2 - square_width - shaded_width, y_base)
alex.pendown()
for i in range(shaded_width // gradient_thickness):
    red += red_step
    green += green_step
    blue += blue_step
    alex.pencolor(int(red), int(green), int(blue))
    alex.fillcolor(int(red), int(green), int(blue))
    alex.begin_fill()
    alex.forward(square_height)
    alex.right(90)
    alex.forward(gradient_thickness)
    alex.right(90)
    alex.forward(square_height)
    alex.right(90)
    alex.forward(gradient_thickness)
    alex.right(180)
    alex.forward(gradient_thickness)
    alex.left(90)
    alex.end_fill()

alex.begin_fill()
alex.forward(square_height)
alex.right(90)
alex.forward(square_width)
alex.right(90)
alex.forward(square_height)
alex.right(90)
alex.forward(square_width)
alex.right(180)
alex.forward(square_width)
alex.left(90)
alex.end_fill()

# Draw balcony of lighthouse
alex.pensize(1)
y_base = -frame_height // 2 + frame_thickness // 2 + square_height
square_height = 20
square_width = 95
shaded_width = 50
initial_red = 99
initial_green = 29
initial_blue = 46
target_red = 0
target_green = 0
target_blue = 0

red_step = (target_red - initial_red) / (shaded_width // gradient_thickness)
green_step = (target_green - initial_green) / (shaded_width // gradient_thickness)
blue_step = (target_blue - initial_blue) / (shaded_width // gradient_thickness)

red = initial_red
green = initial_green
blue = initial_blue

alex.penup()
alex.setheading(90)
alex.setposition(frame_width // 2 - square_width - shaded_width, y_base)
alex.pendown()
for i in range(shaded_width // gradient_thickness):
    red += red_step
    green += green_step
    blue += blue_step
    alex.pencolor(int(red), int(green), int(blue))
    alex.fillcolor(int(red), int(green), int(blue))
    alex.begin_fill()
    alex.forward(square_height)
    alex.right(90)
    alex.forward(gradient_thickness)
    alex.right(90)
    alex.forward(square_height)
    alex.right(90)
    alex.forward(gradient_thickness)
    alex.right(180)
    alex.forward(gradient_thickness)
    alex.left(90)
    alex.end_fill()

alex.begin_fill()
alex.forward(square_height)
alex.right(90)
alex.forward(square_width)
alex.right(90)
alex.forward(square_height)
alex.right(90)
alex.forward(square_width)
alex.right(180)
alex.forward(square_width)
alex.left(90)
alex.end_fill()

# Draw light of lighthouse

# Light of lighthouse left
alex.pensize(1)
y_base = y_base + square_height
delta = 2
square_height = 75
shaded_width = 10
initial_red = 230
initial_green = 230
initial_blue = 20
target_red = 240
target_green = 240
target_blue = 120

red_step = (target_red - initial_red) / (shaded_width // delta)
green_step = (target_green - initial_green) / (shaded_width // delta)
blue_step = (target_blue - initial_blue) / (shaded_width // delta)

red = initial_red
green = initial_green
blue = initial_blue

alex.penup()
alex.setheading(90)
alex.setposition(frame_width // 2 - shaded_width - 63, y_base)
alex.pendown()
for i in range(shaded_width // delta):
    red += red_step
    green += green_step
    blue += blue_step
    alex.pencolor(int(red), int(green), int(blue))
    alex.fillcolor(int(red), int(green), int(blue))
    alex.begin_fill()
    alex.forward(square_height)
    alex.right(90)
    alex.forward(delta)
    alex.right(90)
    alex.forward(square_height)
    alex.right(90)
    alex.forward(delta)
    alex.right(180)
    alex.forward(delta)
    alex.left(90)
    alex.end_fill()
    
# Light of lighthouse right
for i in range(shaded_width // delta):
    red -= red_step
    green -= green_step
    blue -= blue_step
    alex.pencolor(int(red), int(green), int(blue))
    alex.fillcolor(int(red), int(green), int(blue))
    alex.begin_fill()
    alex.forward(square_height)
    alex.right(90)
    alex.forward(delta)
    alex.right(90)
    alex.forward(square_height)
    alex.right(90)
    alex.forward(delta)
    alex.right(180)
    alex.forward(delta)
    alex.left(90)
    alex.end_fill()


# Create lighthouse bars
square_height = 75
square_width = 6
bar_gap = 37
alex.penup()
alex.setheading(90)
alex.setposition(410, y_base)
alex.pendown()
alex.pencolor("black")
alex.fillcolor("black")

for i in range(3):
    alex.begin_fill()
    alex.forward(square_height)
    alex.right(90)
    alex.forward(square_width)
    alex.right(90)
    alex.forward(square_height)
    alex.end_fill()

    alex.left(90)
    alex.forward(bar_gap)
    alex.left(90)

# Draw ceiling of lighthouse
alex.pensize(1)
y_base += square_height
square_height = 20
square_width = 95
shaded_width = 45
initial_red = 99
initial_green = 29
initial_blue = 46
target_red = 0
target_green = 0
target_blue = 0

red_step = (target_red - initial_red) / (shaded_width // gradient_thickness)
green_step = (target_green - initial_green) / (shaded_width // gradient_thickness)
blue_step = (target_blue - initial_blue) / (shaded_width // gradient_thickness)

red = initial_red
green = initial_green
blue = initial_blue

alex.penup()
alex.setheading(90)
alex.setposition(frame_width // 2 - square_width - shaded_width, y_base)
alex.pendown()
for i in range(shaded_width // gradient_thickness):
    red += red_step
    green += green_step
    blue += blue_step
    alex.pencolor(int(red), int(green), int(blue))
    alex.fillcolor(int(red), int(green), int(blue))
    alex.begin_fill()
    alex.forward(square_height)
    alex.right(90)
    alex.forward(gradient_thickness)
    alex.right(90)
    alex.forward(square_height)
    alex.right(90)
    alex.forward(gradient_thickness)
    alex.right(180)
    alex.forward(gradient_thickness)
    alex.left(90)
    alex.end_fill()

alex.begin_fill()
alex.forward(square_height)
alex.right(90)
alex.forward(square_width)
alex.right(90)
alex.forward(square_height)
alex.right(90)
alex.forward(square_width)
alex.right(180)
alex.forward(square_width)
alex.left(90)
alex.end_fill()


# Draw dome of lighthouse
alex.pensize(1)
y_base += square_height
delta = 2
stretch = .5
radius = 45
x = -int((radius**2 / stretch)**0.5)
width = -x * 2
shaded_width = 40
initial_red = 99
initial_green = 29
initial_blue = 46
target_red = 0
target_green = 0
target_blue = 0

red_step = (target_red - initial_red) / (shaded_width // delta)
green_step = (target_green - initial_green) / (shaded_width // delta)
blue_step = (target_blue - initial_blue) / (shaded_width // delta)

red = initial_red
green = initial_green
blue = initial_blue

alex.penup()
alex.setheading(0)
alex.setposition(frame_width // 2 - width, y_base)
alex.pendown()

for i in range(shaded_width // delta):
    red += red_step
    green += green_step
    blue += blue_step
    alex.pencolor(int(red), int(green), int(blue))
    alex.fillcolor(int(red), int(green), int(blue))
    # Use equation of an ellipse get dome curve
    y = int((radius**2 - stretch*x**2)**0.5)
    alex.begin_fill()
    alex.left(90)
    alex.forward(y)
    alex.right(90)
    alex.forward(delta)
    alex.right(90)
    alex.forward(y)
    alex.left(90)
    alex.end_fill()
    x += delta

for i in range((width - shaded_width) // delta):
    y = int((radius**2 - stretch*x**2)**0.5)
    alex.begin_fill()
    alex.left(90)
    alex.forward(y)
    alex.right(90)
    alex.forward(delta)
    alex.right(90)
    alex.forward(y)
    alex.left(90)
    alex.end_fill()
    x += delta

# Draw top of lighthouse
alex.pensize(1)
y_base += radius
delta = 1
square_height = 18
square_width = 4
shaded_width = 4
initial_red = 99
initial_green = 29
initial_blue = 46
target_red = 0
target_green = 0
target_blue = 0

red_step = (target_red - initial_red) / (shaded_width // delta)
green_step = (target_green - initial_green) / (shaded_width // delta)
blue_step = (target_blue - initial_blue) / (shaded_width // delta)

red = initial_red
green = initial_green
blue = initial_blue

alex.penup()
alex.setheading(90)
alex.setposition(frame_width // 2 - square_width - shaded_width - 57, y_base)
alex.pendown()
for i in range(shaded_width // delta):
    red += red_step
    green += green_step
    blue += blue_step
    alex.pencolor(int(red), int(green), int(blue))
    alex.fillcolor(int(red), int(green), int(blue))
    alex.begin_fill()
    alex.forward(square_height)
    alex.right(90)
    alex.forward(delta)
    alex.right(90)
    alex.forward(square_height)
    alex.right(90)
    alex.forward(gradient_thickness)
    alex.right(180)
    alex.forward(gradient_thickness)
    alex.left(90)
    alex.end_fill()

alex.begin_fill()
alex.forward(square_height)
alex.right(90)
alex.forward(square_width)
alex.right(90)
alex.forward(square_height)
alex.right(90)
alex.forward(square_width)
alex.right(180)
alex.forward(square_width)
alex.left(90)
alex.end_fill()

# Draw Docks
alex.pensize(25)
alex.fillcolor("black")
alex.penup()
alex.setposition(-frame_width // 2, -frame_height // 2)
alex.pendown()
alex.begin_fill()
alex.setheading(90)
alex.forward(60)
alex.right(90)
alex.forward(270)
alex.right(90)
alex.forward(20)
alex.left(90)
alex.forward(50)
alex.right(90)
alex.forward(15)
alex.left(90)
alex.forward(490)
alex.left(90)
alex.forward(25)
alex.right(90)
alex.forward(65)
alex.left(90)
alex.forward(25)
alex.right(90)
alex.forward(190)
alex.right(90)
alex.forward(75)
alex.right(90)
alex.forward(1060)
alex.end_fill()

# Draw person fishing
alex.pencolor("black")
alex.pensize(25)
alex.penup()
alex.setposition(265, -220)
alex.pendown()
alex.setheading(0)

# Body
alex.begin_fill()
alex.forward(30)
alex.left(90)
alex.forward(40)
alex.left(90)
alex.forward(30)
alex.left(90)
alex.forward(40)
alex.end_fill()

# Head
alex.left(180)
alex.forward(40)
alex.right(90)
alex.forward(12)
alex.left(90)
alex.forward(30)
alex.right(90)
alex.forward(8)
alex.right(90)
alex.forward(30)

# Hat
alex.begin_fill()
alex.right(180)
alex.forward(35)
alex.right(90)
alex.pensize(10)
alex.forward(20)
alex.left(90)
alex.forward(5)
alex.left(90)
alex.forward(15)
alex.right(90)
alex.forward(20)
alex.left(90)
alex.forward(15)
alex.left(90)
alex.forward(20)
alex.right(90)
alex.forward(15)
alex.left(90)
alex.forward(5)
alex.left(90)
alex.forward(20)
alex.end_fill()

# Legs
alex.pensize(18)
alex.penup()
alex.setposition(265, -220)
alex.pendown()
alex.setheading(180)
alex.forward(23)
alex.left(90)
alex.forward(23)


# Fishing rod
alex.pensize(5)
alex.penup()
alex.setposition(265, -210)
alex.pendown()
alex.setheading(90)
alex.forward(25)
alex.left(65)
alex.forward(85)

alex.pensize(1)
alex.left(105)
alex.forward(120)

# Draw Sign
alex.pensize(7)
alex.penup()
alex.setposition(-170, -245)
alex.pendown()
alex.setheading(90)
alex.forward(25)

alex.pensize(16)
alex.left(90)
alex.forward(7)
alex.left(180)
alex.forward(40)
alex.left(180)
alex.forward(7)

alex.pensize(7)
alex.left(90)
alex.forward(35)

# Draw frame again
alex.penup()
alex.setposition(frame_width / 2, 0)
alex.setheading(90)
alex.pendown()
alex.pensize(frame_thickness)
alex.forward(frame_height / 2)
alex.left(90)
alex.forward(frame_width)
alex.left(90)
alex.forward(frame_height)
alex.left(90)
alex.forward(frame_width)
alex.left(90)
alex.forward(frame_height - 5)
alex.left(90)

window.exitonclick()
