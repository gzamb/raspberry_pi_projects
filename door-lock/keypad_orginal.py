# #####################################################
# Python Library for 3x4 matrix keypad using
# 7 of the available GPIO pins on the Raspberry Pi.
# 
# This could easily be expanded to handle a 4x4 but I 
# don't have one for testing. The KEYPAD constant 
# would need to be updated. Also the setting/checking
# of the colVal part would need to be expanded to 
# handle the extra column.
# 
# Written by Chris Crumpacker
# May 2013
#
# main structure is adapted from Bandono's
# matrixQPI which is wiringPi based.
# https://github.com/bandono/matrixQPi?source=cc
# #####################################################

import RPi.GPIO as GPIO
from time import sleep


class Keypad:
    KEYPAD = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9'],
        ["*", '0', "#"]
    ]

    ROW = [27, 26, 19, 6]
    COLUMN = [22, 17, 13]

    def __init__(self):
        print('Initializing Keypad class')
        self.code = ''
        GPIO.setmode(GPIO.BCM)
    
    def get_key(self):
        # Set all columns as output low
        for j in range(len(self.COLUMN)):
            GPIO.setup(self.COLUMN[j], GPIO.OUT)
            GPIO.output(self.COLUMN[j], GPIO.LOW)
        
        # Set all rows as input
        for i in range(len(self.ROW)):
            GPIO.setup(self.ROW[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
        # Scan rows for pushed key/button
        # A valid key press should set "row_val"  between 0 and 3.
        row_val = -1
        for i in range(len(self.ROW)):
            tmp_read = GPIO.input(self.ROW[i])
            if tmp_read == 0:
                row_val = i
                
        # if row_val is not 0 through 3 then no button was pressed and we can exit
        if row_val < 0 or row_val > 3:
            self.exit()
            return
        
        # Convert columns to input
        for j in range(len(self.COLUMN)):
                GPIO.setup(self.COLUMN[j], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        
        # Switch the i-th row found from scan to output
        GPIO.setup(self.ROW[row_val], GPIO.OUT)
        GPIO.output(self.ROW[row_val], GPIO.HIGH)

        # Scan columns for still-pushed key/button
        # A valid key press should set "col_val"  between 0 and 2.
        col_val = -1
        for j in range(len(self.COLUMN)):
            tmp_read = GPIO.input(self.COLUMN[j])
            if tmp_read == 1:
                col_val=j
                
        # if col_val is not 0 through 2 then no button was pressed and we can exit
        if col_val < 0 or col_val > 2:
            self.exit()
            return

        # Return the value of the key pressed
        self.exit()
        return self.KEYPAD[row_val][col_val]

    def get_input(self):
        while len(self.code) != 4:
            digit = None
            while digit is None:
                digit = self.get_key()
            sleep(1)
            self.code += digit
        return self.code

    def clear_code(self):
        self.code = ''

    def exit(self):
        # Reinitialize all rows and columns as input at exit
        for i in range(len(self.ROW)):
                GPIO.setup(self.ROW[i], GPIO.IN, pull_up_down=GPIO.PUD_UP) 
        for j in range(len(self.COLUMN)):
                GPIO.setup(self.COLUMN[j], GPIO.IN, pull_up_down=GPIO.PUD_UP)
