import  unittest

from src.Weapon import Weapon
from src.Blaster import Blaster
from src.Container import Container
from src.HybridShip import HybridShip
from src.LightWeightWarShip import LightWeightWarShip
from src.Phaser import Phaser
from src.TransportShip import TransportShip


class TeacherScenarioTest(unittest.TestCase):

    def setUp(self):
        self.phasers = []

        self.vc1 = LightWeightWarShip(10, 50, 2)
        print 'Soit un vaisseau de combat leger' + self.vc1.name + '(volume=10, masse=50, 2 armes max)'
        print 'On equipe' + self.vc1.name + ' avec deux phasers (volume=1, masse=1)'

        p = Phaser(1, 1)
        p1 = Phaser(1, 1)

        self.vc1.load(p)
        self.vc1.load(p1)

        self.phasers.append(p)
        self.phasers.append(p1)

        self.vt2 = TransportShip(100, 100, 90, 300)
        print 'Soit un vaisseau de transport ' + self.vt2.name + \
              ' (volume=100, masse=100, cap_volume=90, cap_masse=300)'

        print 'On charge ' + self.vt2.name + ' avec 5 conteneurs (volume=1, masse= 1)'

        for i in range (0, 5):
            self.vt2.load(Container(1,1))

        print 'On charge ' + self.vt2.name + ' avec ' + self.vc1.name + ' comme du fret'

        self.vt2.load(self.vc1)

        print 'On desequipe un des phasers de ' + self.vc1.name + ' et ' \
              'on le charge dans ' + self.vt2.name + ' comme du fret'

        self.vc1.unload(p)
        self.vt2.load(p)

        self.mr63 = HybridShip(200, 150, 180, 600, 5)
        print 'Soit ' + self.mr63.name + ' un vieux modele de vaisseau de transport lourd capable de se battre ' \
              '(volume=200, masse=150, cap_volume=180, cap_masse=600, 5 armes max)'

        print 'On equipe ' + self.mr63.name + ' avec deux blasters (volume=2, masse=2, gaz=50%),' \
              ' deux phasers (volume=1, masse=1),' \
              ' le vaisseau ' + self.vt2.name + \
              ' et 4 conteneurs (volume=10, masse=100)'

        b = Blaster(2, 2, 50)
        b2 = Blaster(2, 2, 50)

        self.mr63.load(b)
        self.mr63.load(b2)

        p2 = Phaser(1,1)
        p3 = Phaser(1,1)

        self.phasers.append(p2)
        self.phasers.append(p3)

        self.mr63.load(p2)
        self.mr63.load(p3)

        self.mr63.load(self.vt2)

        for i in range(0, 4):
            self.mr63.load(Container(10, 100))

        print 'On veut connaitre le niveau de gaz des blasters equipes par ' + self.mr63.name + ', puis les recharger'

        for equipment in self.mr63.equipments:
            if isinstance(equipment, Blaster):
                print 'Niveau de gaz de ' + equipment.name + ': ' + str(equipment.gaz_level)
                equipment.recharge()
                print 'Niveau de gaz de ' + equipment.name + ' apres rechargement: ' + str(equipment.gaz_level)

    def resolveLocation(self, equipment):
        if equipment.location is None:
            return

        if isinstance(equipment, Weapon) and equipment.equipped:
            print equipment.name + ' est equipe par ' + equipment.location.name
        else:
            print equipment.name + ' est dans la soute de ' + equipment.location.name

        self.resolveLocation(equipment.location)

    def tearDown(self):
        self.vc1 = None
        self.mr63 = None
        self.vt2 = None
        self.phasers = None

    def test_total_mass_total_volume_of_mr_63(self):
        print 'On veut savoir quelle est la masse total de ' + self.mr63.name + \
              ' (un bon 713) et quel est le volume disponible dans MR-63 (il en reste pour 34)'

        print 'Masse de ' + self.mr63.name + ': ' + str(self.mr63.mass)
        print 'Volume disponible de ' + self.mr63.name + ': ' + str(self.mr63.volume_capacity_remaining)

    def test_where_are_the_phasers(self):
        print 'On veut savoir ou est chacun des phasers (deux sont dans ' + self.mr63.name + \
              ', un dans la soute de ' + self.vt2.name + ', le dernier est equipe par ' + \
              self.vc1.name + ')'

        for phaser in self.phasers:
            self.resolveLocation(phaser)
