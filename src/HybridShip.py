from src.TransportShip import TransportShip
from src.WarShip import WarShip


class HybridShip(TransportShip, WarShip):

    def __init__(self, volume, mass, volume_capacity, weight_capacity, max_nb_weapons):
        TransportShip.__init__(self, volume, mass, volume_capacity, weight_capacity)
        WarShip.__init__(self, volume, mass, max_nb_weapons)

    def equip(self, weapon):
        WarShip.load(self, weapon)

    def unequip(self, weapon):
        WarShip.unload(self, weapon)
