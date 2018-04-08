#!/usr/bin/env python

"""
Door Lock: System to control an electric door lock.
"""
from time import sleep
# from .keypad import Keypad
from .keypad_orginal import Keypad


class AuthToken:
    def __init__(self, secret):
        # self.user = user
        self.secret = secret


class TestDoorController:
    def send_open_pulse(self):
        print('unlock, wait, relock')


class TestInput:
    def get_input(self):
        print('checking for input')
        auth_token = AuthToken('Gorilla', '1234')
        return auth_token


class BasicAuthenticator:
    user = 'Gorilla'
    secret_password = '1234'

    def check(self, token):
        #print(f'checking input of "{token.user}", password: "{token.secret}", against '
        #      f'secret_password "{self.secret_password}"')
        print('checking input of "' + token.user + '", password: "' + token.secret +
                '", against secret password "' + self.secret_password + '"')
        result = token.secret == self.secret_password and token.user == self.user
        #print(f'authentication is: {result}')
        print('authentication is: ' + result)
        return result


class DoorController:
    def send_open_pulse(self):
        # turn on led
        sleep(5) # sleep for 5 seconds
        # turn off led
        pass


class DoorControllerLED:
    from gpiozero import LED
    red = LED(4)   # Change to whatever pin LED is hooked up

    def send_open_pulse(self):
        # turn on led
        self.red.on()
        # sleep for 5 seconds
        sleep(5)
        # turn off led
        self.red.off()


class KeyboardInput:
    def get_input(self):
        print('checking for input')
        user = input('Please enter your name: ')
        password = input('Please enter your password: ')
        auth_token = AuthToken(user, password)
        return auth_token


class FileAuthentication:
    filename = 'secrets.txt'

    def _check_file(self, user, secret):
        with open(self.filename, 'r') as f:
            for line in f.readlines():
                name, secret_password = [x.strip() for x in line.rstrip('\n').split(',')]
                if name == user and secret == secret_password:
                    return True
            return False

    def check(self, token):
        #print(f'checking input of "{token.user}", password: "{token.secret}", against system.')
        print('checking password: "' + token.secret + '", against system.')
        result = self._check_file(token.user, token.secret)
        #print(f'authentication is: {result}')
        print('authentication is: ' + result)
        return result


def main():
    auth_input = Keypad()
    # auth_input = KeyboardInput()            # TestInput()
    authenticator = FileAuthentication()    # BasicAuthenticator()
    door_controller = DoorControllerLED()  # DoorController()

    if authenticator.check(auth_input.get_input()):
        door_controller.send_open_pulse()


if __name__ == '__main__':
    main()
