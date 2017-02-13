from src.Weapon import Weapon
from src.Ship import Ship


class WarShip(Ship):
    _nb_instances = 0

    def __init__(self, volume, mass, max_nb_weapons):
        super(WarShip, self).__init__(volume, mass)
        self._max_nb_weapons = max_nb_weapons
        WarShip._nb_instances += 1
        self.name = "VC-" + str(self._nb_instances)

    @property
    def max_nb_weapons(self):
        return self._max_nb_weapons

    def load(self, weapon):
        assert isinstance(weapon, Weapon), 'WarShip can only load Weapon object.'
        assert len(self.equipments) + 1 <= self._max_nb_weapons, 'Impossible to add more weapon: ' \
                                                                 'maximum number of weapons reached for this WarShip'

        Ship.load(self, weapon)

        weapon.equipped = True

    def unload(self, weapon):
        super(WarShip, self).unload(weapon)
        weapon.equipped = False
