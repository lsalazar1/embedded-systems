'''
    Author: Liam Salazar
    Date: February 14, 2020
'''
from random import randint
from time import sleep
from sense_hat import SenseHat

class senseHAT:
    def __init__(self):
        self.sense = SenseHat()
        self.red = (255, 0 , 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.lightGreen = (70, 255, 102)
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
    
    # Display a message using user input with orange text & black background
    def displayText(self):
        textColor = (253, 95, 0)
        message = input('Enter a message to display: ')

        self.sense.show_message(message, text_colour = textColor, back_colour = self.black)

    # Given any word, this method will display each char every x seconds in red
    def displayChars(self, word, x):
        for letter in word:
            self.sense.show_letter(letter, text_colour = self.red)
            sleep(x)
    
    # Lights the entire board light green
    def makeOneColor(self):
        self.sense.clear(self.lightGreen)
    
    # Makes a happy face by setting individual pixels
    def onePixel(self):
        self.sense.set_pixel(2, 2, self.blue)
        self.sense.set_pixel(4, 2, self.blue)
        self.sense.set_pixel(3, 4, self.lightGreen)
        self.sense.set_pixel(1, 5, self.red)
        self.sense.set_pixel(2, 6, self.red)
        self.sense.set_pixel(3, 6, self.red)
        self.sense.set_pixel(4, 6, self.red)
        self.sense.set_pixel(5, 5, self.red)

    # Lights up entire LED Board based on list
    def manyPixels(self):
        matrix = []

        # Appends black or white into matrix based on number value
        while len(matrix) < 64:
            randNum = randint(0, 1)

            if randNum == 0:
                matrix.append(self.black)
            
            matrix.append(self.white)
        
        self.sense.set_pixels(matrix)
    
    # Given an orientation, LED Matrix will either be flipped horizontally, vertically, or rotated
    def setOrientation(self, option):
        w = (150, 150, 150)
        e = self.white
        b = self.blue

        image = [
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e,
            w,w,w,e,e,w,w,w,
            w,w,b,e,e,w,w,b,
            w,w,w,e,e,w,w,w,
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e
        ]

        if option == 'horizontal':
            for i in range(5):
                self.sense.flip_h()
        elif option == 'vertical':
            for i in range(5):
                self.sense.flip_v()
        elif option == 'rotate':
            rotation = int(input('Enter degrees to rotate: '))
            self.sense.set_rotation(rotation)

    # Output environment details to LED Matrix
    def getEnironment(self):
        # get_temperature() returns celsius... convert this to farenheit
        temp = self.sense.get_temperature() * 1.8 + 32
        humidty = self.sense.get_humidity()
        pressure = self.sense.get_pressure()

        tempMessage = "Temperature: " + str(temp) + "F"
        humidtyMessage = "Humidity: " + str(humidty) + "%"
        pressureMessage = "Pressue: " + str(pressure) + "millibars"

        self.sense.show_message(tempMessage)
        sleep(1)
        self.sense.show_message(humidtyMessage)
        sleep(1)
        self.sense.show_message(pressureMessage)
        sleep(1)

        # Will water freeze right now?
        if temp <= 32:
            self.sense.show_message('Water will freeze at current temp')
        else:
            self.sense.show_message('Water will not freeze right now')

