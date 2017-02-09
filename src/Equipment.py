class Equipment:

    def __init__(self, volume, mass):
        self.location = None
        self.name = None
        self.volume = volume
        self.mass = mass

    def getName(self):
        return self.name

    def getVolume(self):
        return self.volume

    def getMass(self):
        return self.mass

    def getLocation(self):
        return self.location

    def setLocation(self, location):
        self.location = location