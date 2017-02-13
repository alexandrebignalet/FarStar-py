from src.TransportShip import TransportShip
from src.WarShip import WarShip


class HybridShip(TransportShip, WarShip):
    _nb_instances = 0

    def __init__(self, volume, mass, volume_capacity, weight_capacity, max_nb_weapons):
        TransportShip.__init__(self, volume, mass, volume_capacity, weight_capacity)
        WarShip.__init__(self, volume, mass, max_nb_weapons)
        HybridShip._nb_instances += 1
        self.name = "MR-"+str(HybridShip._nb_instances)

    def equip(self, weapon):
        WarShip.load(self, weapon)

    def unequip(self, weapon):
        WarShip.unload(self, weapon)
