from device import *
from errorhandler import FlashFaliureException

class Iflashdevice:
    def flashdevice(self):
        pass
    
class flashdevice(Iflashdevice):
    def __init__(self, device: device):
        self.device = device

    def flashdevice(self):
        try:
            self.device.flashdevice()
        except:
            raise FlashFaliureException

