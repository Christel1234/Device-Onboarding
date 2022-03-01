from device import *
from errorhandler import InjectionFaliureException

class Ikeyinjection:
    def keyinjection(self):
        pass

class keyinjection(Ikeyinjection):
    def __init__(self, key):
        self.key = key

    def injectkey(self, key):
        try:
            self.injectkey(key)
            return True
        except:
            raise InjectionFaliureException
