from time import sleep
from gpiozero import OutputDevice

# Simple code for controlling lock relay
# The module I have uses an active low signal to activate the relay
# Lock(pin, pulse=200)
class Lock:

    def __init__(self, pin, pulse=100):
        self._output = OutputDevice(pin=pin, active_high=False, initial_value=False)
        self._pulse = pulse

    def unlock(self):
        self._output.on()
        sleep(self._pulse/1000)
        self._output.off()
