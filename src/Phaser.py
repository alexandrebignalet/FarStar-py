from src.Weapon import Weapon


class Phaser(Weapon):

    _nb_instances = 0

    def __init__(self, volume, mass):
        super(Phaser, self).__init__(volume, mass)
        Phaser._nb_instances += 1
        self.name = "P-" + str(Phaser._nb_instances)
