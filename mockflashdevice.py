from device import *
from errorhandler import FlashFaliureException

class Iflashdevice:
    def flashdevice(self):
        pass
class flashdevice(Iflashdevice):
    def __init__(self, state):
        self.state = state 
    def flashdevice(self):
        if self.state >= 1: 
            return True
        else:
            raise FlashFaliureException

