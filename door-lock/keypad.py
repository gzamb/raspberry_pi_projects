# #####################################################
# Python Library for 3x4 matrix keypad using
# 7 of the available GPIO pins on the Raspberry Pi.
#
# #####################################################

# import RPi.GPIO as GPIO
from gpiozero import DigitalInputDevice, DigitalOutputDevice


class Keypad:
    KEYPAD = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9'],
        ['*', '0', '#'],
    ]

    # These should correspond to the actual GPIO pin
    # numbers that the keypad is hooked up to on the pi.
    #ROWS = [5, 6, 7, 8],
    #COLUMNS = [2, 3, 4],
    ROWS = [27, 6, 14, 26]
    COLUMNS = [12, 22, 13]

    def __init__(self):
        # Nothing really goes here yet
        pass

    def get_key(self):
        # Set all columns as output low
        for j in range(len(self.COLUMNS)):
            DigitalOutputDevice(self.COLUMNS[j], active_high=False)
            # GPIO.setup(self.COLUMNS[j], GPIO.OUT)
            # GPIO.output(self.COLUMNS[j], GPIO.LOW)

        # Set all rows as input
        for i in range(len(self.ROWS)):
            DigitalInputDevice(self.ROWS[i], pull_up=True)
            # GPIO.setup(self.ROW[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)

        # Scan rows for pushed key/button
        # A valid key press should set "row_val" between 0 and 3.
        row_val = -1
        for i in range(len(self.ROWS)):
            # tmpRead = GPIO.input(self.ROWS[i])
            tmp_read = DigitalInputDevice(self.ROWS[i]).is_active
            if tmp_read == 0:
                row_val = i

        # if row_val is not 0 through 3 then no button was pressed and we can exit
        if row_val < 0 or row_val > 3:
            self.exit()
            return

        # Convert columns to input
        for j in range(len(self.COLUMNS)):
            # GPIO.setup(self.COLUMN[j], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
            DigitalInputDevice(self.COLUMNS[j], pull_up=True)

        # Switch the i-th row found from scan to output
        DigitalOutputDevice(self.ROWS[row_val], active_high=True)
        # GPIO.setup(self.ROW[row_val], GPIO.OUT)
        # GPIO.output(self.ROW[row_val], GPIO.HIGH)

        # Scan columns for still-pushed key/button
        # A valid key press should set "col_val"  between 0 and 2.
        col_val = -1
        for j in range(len(self.COLUMNS)):
            tmp_read = DigitalOutputDevice(self.COLUMNS[j]).is_active
            # tmpRead = GPIO.input(self.COLUMN[j])
            if tmp_read == 1:
                col_val = j

        # if col_val is not 0 thru 2 then no button was pressed and we can exit
        if col_val < 0 or col_val > 2:
            self.exit()
            return

        # Return the value of the key pressed
        self.exit()
        return self.KEYPAD[row_val][col_val]

    def exit(self):
        # Reinitialize all rows and columns as input at exit
        for i in range(len(self.ROWS)):
            DigitalInputDevice(self.ROWS[i], pull_up=True)
            # GPIO.setup(self.ROW[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)
        for j in range(len(self.COLUMNS)):
            DigitalInputDevice(self.COLUMNS[j], pull_up=True)
            # GPIO.setup(self.COLUMN[j], GPIO.IN, pull_up_down=GPIO.PUD_UP)


if __name__ == '__main__':
    # Initialize the keypad class
    kp = Keypad()

    # Loop while waiting for a keypress
    digit = None
    while digit is None:
        digit = kp.get_key()

    # Print the result
    print(digit)
