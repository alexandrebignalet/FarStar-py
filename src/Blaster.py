from src.Weapon import Weapon


class Blaster(Weapon):

    _MAX_PERCENT_GAZ_LEVEL = 100
    _nb_instances = 0

    def __init__(self, volume, mass, gaz_level):
        Weapon.__init__(self, volume, mass)
        self._gaz_level = gaz_level
        self._nb_instances += 1
        self._name = "B-" + str(self._nb_instances)

    @property
    def gaz_level(self):
        return self._gaz_level

    def recharge(self):
        self._gaz_level = self._MAX_PERCENT_GAZ_LEVEL
