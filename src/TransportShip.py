from src.Equipment import Equipment
from src.Ship import Ship


class TransportShip(Ship):
    _nb_instances = 0

    def __init__(self, volume, mass, volume_capacity, weight_capacity):

        assert volume_capacity < volume, 'Transport ship volume capacity must be lower than volume.'

        Ship.__init__(self, volume, mass)

        self._volume_capacity = volume_capacity
        self._weight_capacity = weight_capacity

        self._volume_capacity_remaining = volume_capacity
        self._weight_capacity_remaining = weight_capacity

        TransportShip._nb_instances += 1
        self.name = "VT-" + str(TransportShip._nb_instances)

    def load(self, equipment):
        assert isinstance(equipment, Equipment), 'A transport ship can only load Equipment object'
        assert self._volume_capacity_remaining >= equipment.volume, 'There is not enough volume space ' \
                                                                   'in the transport ship to load this equipment'

        assert self._weight_capacity_remaining >= equipment.mass, 'There is not enough weight capacity remaining in ' \
                                                                 'the transport ship to load this equipment'

        Ship.load(self, equipment)

        self._volume_capacity_remaining -= equipment.volume
        self._weight_capacity_remaining -= equipment.mass

    def unload(self, equipment):
        super(TransportShip, self).unload(equipment)
        self._volume_capacity_remaining += equipment.volume
        self._weight_capacity_remaining += equipment.mass

    @property
    def volume_capacity(self):
        return self._volume_capacity

    @property
    def weight_capacity(self):
        return self._weight_capacity

    @property
    def volume_capacity_remaining(self):
        return self._volume_capacity_remaining

    @property
    def weight_capacity_remaining(self):
        return self._weight_capacity_remaining