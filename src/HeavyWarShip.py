from src.WarShip import WarShip


class HeavyWarShip(WarShip):

    def __init__(self, volume, mass, max_nb_weapons):
        super(HeavyWarShip, self).__init__(volume, mass, max_nb_weapons)