from src.Phaser import Phaser
from src.WarShip import WarShip


class LightWeightWarShip(WarShip):

    def __init__(self, volume, mass, max_nb_weapons):
        super(LightWeightWarShip, self).__init__(volume, mass, max_nb_weapons)

    def load(self, equipment):
        assert isinstance(equipment, Phaser)
        super(LightWeightWarShip, self).load(equipment)