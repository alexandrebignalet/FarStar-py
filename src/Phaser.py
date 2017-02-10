from src.Weapon import Weapon


class Phaser(Weapon):

    _nbInstances = 0

    def __init__(self, volume, mass):
        Weapon.__init__(self, volume, mass)
        self._nbInstances += 1
        self._name = "P-" + str(self._nbInstances)
