from device import *
from errorhandler import FlashFaliureException

class Iflashdevice:
    def flashdevice(self):
        pass
class flashdevice(Iflashdevice):
    def __init__(self, device):
        self.device = device
    def flashdevice(self):
        try:
            self.flashdevice()
        except:
            raise FlashFaliureException

