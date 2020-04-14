'''
Author: Liam Salazar
Date: April 12, 2020
'''
from sense_hat import SenseHat
from time import sleep
from math import ceil

import sys

def check_overflow():
  '''
  This function is used in the program to see if the RGB values exceed 255. If any
  of the values are over 255, the Sense HAT will output a message and exit the program with
  status 0.

  @params: red, blue, green
  @return: None
  '''
  global red, blue, green
  
  if red > 255 or green > 255 or blue > 255:
    sense.show_message('Exit program')
    sys.exit(0)

sense = SenseHat()

# Initial RGB values
red = 0
blue = 0
green = 0

# These XYZ vars are used to see any changes in motion. Initialiazed at 0.
old_x = 0
old_y = 0
old_z = 0

try:
    while True:
        acc = sense.get_accelerometer_raw()
        
        # These XYZ values are taken from the IMU. Each value will only show the ceiling value
        x = ceil(acc['x'])
        y = ceil(acc['y'])
        z = ceil(acc['z'])
        
        # If there are any changes in the values, the color corresponding with it will increment by 20
        if old_x != x:
          red += 20
          
        if old_y != y:
          green += 20
          
        if old_z != z:
          blue += 20
        
        # After comparison, the value will be saved for later comparison
        old_x = x
        old_y = y
        old_z = z
        
        # To show values being used for LED Matrix
        print('{} {} {}'.format(red, green, blue))
        
        check_overflow()
        
        # Use RGB values in a list to display in LED Matrix, then sleep for 1 second before starting new loop
        sense.clear([red, green, blue])
        sleep(1)
except KeyboardInterrupt:
  '''
  A keyboard interrupt (CTRL + C) allows the user to end the program. The
  sense HAT will display a message at the end.
  '''
  sense.show_message('Exiting Program')