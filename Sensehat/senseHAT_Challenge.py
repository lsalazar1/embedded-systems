from sense_hat import SenseHat
from time import sleep
from random import choice

# Function sets pixels to look like an arrow given a color param
def arrow(c):
    a = [
        black, black, black, c, black, black, black, black,
        black, black, c, c, c, black, black, black,
        black, c, c, c, c, c, black, black,
        c, c, c, c, c, c, c, black,
        black, black, c, c, c, black, black, black,
        black, black, c, c, c, black, black, black,
        black, black, c, c, c, black, black, black,
        black, black, black, black, black, black, black,black
    ]
    
    return a

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
    
    x = round(acceleration['x'], 0)
    y = round(acceleration['y'], 0)
    z = round(acceleration['z'], 0)
    
    if x == -1 and angle == 180:
        sense.set_pixels(greenArrow)
        score += 1
    elif x == 1 and angle == 0:
        sense.set_pixels(greenArrow)
        score += 1
    elif y == -1 and angle == 90:
        sense.set_pixels(greenArrow)
        score += 1
    elif y == 1 and angle == 270:
        sense.set_pixels(greenArrow)
        score += 1
    else:
        sense.set_pixels(redArrow)
        play = False
    
    pause = pause * 0.95
    
    sleep(1)
    
msg = "Score: {}".format(score)
sense.show_message(msg, text_colour=red, back_colour = white)