from errorhandler import InjectionFaliureException

class Ikeyinjection:
    def keyinjection(self):
        pass

class keyinjection(Ikeyinjection):
    def __init__(self, state):
        self.state = state

    def injectkey(self, key):
        if self.state == True:
            return True
        else:
            raise InjectionFaliureException
