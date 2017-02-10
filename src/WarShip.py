from src.Weapon import Weapon
from src.Ship import Ship


class WarShip(Ship):

    def __init__(self, volume, mass, max_nb_weapons):
        Ship.__init__(self, volume, mass)
        self._max_nb_weapons = max_nb_weapons

    @property
    def max_nb_weapons(self):
        return self._max_nb_weapons

    def load(self, equipment):
        assert isinstance(equipment, Weapon), 'WarShip can only load Weapon object.'
        assert equipment.location is None, 'Weapon already load elsewhere.'
        assert len(self.equipments) + 1 <= self._max_nb_weapons, 'Impossible to add more weapon: ' \
                                                                'maximum number of weapons reached for this WarShip'

        self.equipments.append(equipment)
        equipment.location = self
