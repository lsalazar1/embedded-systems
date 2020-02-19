from sense_hat import SenseHat
from time import sleep
from random import choice

# Function sets pixels to look like an arrow given a color param
def arrow(c):
    arrow = [
        0, 0, 0, c, 0, 0, 0, 0,
        0, 0, c, c, c, 0, 0, 0,
        0, c, c, c, c, c, 0, 0,
        c, c, c, c, c, c, c, 0,
        0, 0, c, c, c, 0, 0, 0,
        0, 0, c, c, c, 0, 0, 0,
        0, 0, c, c, c, 0, 0, 0
    ]

    return arrow

# Create sensehat obj
sense = SenseHat()

# Declare vars for colours needed
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)

# Create three different colored arrows
redArrow = arrow(red)
whiteArrow = arrow(white)
greenArrow = arrow(green)

# Set pause to 3 for time between runs
pause = 3

score = 0
angle = 0

# play variable is used to stop the game
play = True

while play:
    newAngle = angle
    
    while newAngle == angle:
        angle = choice([0, 90, 180, 270])
    
    sense.set_rotation(angle)
    sense.set_pixels(whiteArrow)

    sleep(pause)

    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']