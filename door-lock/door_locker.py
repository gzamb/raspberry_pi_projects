#!/usr/bin/env python

"""
Door Lock: System to control an electric door lock.
"""
from time import sleep
from gpiozero import LED
from keypad_orginal import Keypad
from lock import Lock

# class DoorController:
#     def send_open_pulse(self):
#         # turn on led
#         sleep(5)    # sleep for 5 seconds
#         # turn off led
#         pass


class DoorControllerLED:
    def __init__(self):
        self.red = LED(4)   # Change to whatever pin LED is hooked up

    def send_open_pulse(self):
        # turn on led
        self.red.on()
        # sleep for 5 seconds
        sleep(5)
        # turn off led
        self.red.off()

class DoorController:
    def __init__(self):
        self.lock = Lock(5)

    def send_open_pulse(self):
        self.lock.unlock()


class FileAuthentication:
    filename = 'secrets.txt'

    def _check_file(self, secret):
        with open(self.filename, 'r') as f:
            for line in f.readlines():
                secret_password = line.strip().rstrip('\n')
                if secret == secret_password:
                    return True
            return False

    def check(self, token):
        print('Checking password: "%s" against system' % token)
        result = self._check_file(token)
        print('authentication is: %s' % str(result))
        return result


def main():
    auth_input = Keypad()
    authenticator = FileAuthentication()
    door_controller = DoorController()

    if authenticator.check(auth_input.get_input()):
        door_controller.send_open_pulse()

    auth_input.clear_code()


if __name__ == '__main__':
    main()
