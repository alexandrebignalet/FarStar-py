from abc import ABCMeta, abstractmethod


class Equipment:
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, volume, mass):
        self._location = None
        self._name = None
        self._volume = volume
        self._mass = mass

    @property
    def volume(self):
        return self._volume

    @property
    def mass(self):
        return self._mass

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, ship):
        from src.Ship import Ship

        if not isinstance(ship, Ship) and ship is not None:
            raise ValueError('Any equipment must be load in a Ship.')

        self._location = ship

    @property
    def name(self):
        return self._name