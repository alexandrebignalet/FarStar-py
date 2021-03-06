from abc import ABCMeta, abstractmethod
from src.Equipment import Equipment


class Ship(Equipment):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, volume, mass):
        super(Ship, self).__init__(volume, mass)
        self._equipments = []

    @property
    def equipments(self):
        return self._equipments

    @property
    def mass(self):
        total = self._mass

        for equipment in self.equipments:
            total += equipment.mass

        return total

    def load(self, equipment):
        assert equipment.location is None, 'Equipment already loaded elsewhere.'

        self.equipments.append(equipment)
        equipment.location = self

    def unload(self, equipment):
        try:
            self._equipments.remove(equipment)
        except ValueError as e:
            raise e
        equipment.location = None

    @Equipment.location.setter
    def location(self, ship):
        from src.TransportShip import TransportShip
        from src.HybridShip import HybridShip

        assert isinstance(ship, TransportShip) or isinstance(ship, HybridShip) or ship is None \
            , 'A Ship can only be located in a TransportShip or in an HybridShip'

        self._location = ship

