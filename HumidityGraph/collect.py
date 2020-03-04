from sense_hat import SenseHat
from time import sleep

# Create a SenseHat Object
sense = SenseHat()

# Store humidity reading from sense into humidity variable
humidity = sense.get_humidity

while True:
    with open('humidity.txt') as f:
        '''
        Open a file called humidity.txt in a variable 
        called f. Each line will have the humidity variable followed
        by an endline, then close.
        '''
        f.write(humidity)
        f.write('\n')
        f.close()