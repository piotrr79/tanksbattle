import sys
import utils.constant as const
from utils.env import EnvReader

sys.tracebacklimit = int(EnvReader.get_traceback_limit())


class Tank:
    """ Class Tank """

    def __init__(self, armor: int, penetration: int, armor_type: str):
      self.armor = armor
      self.penetration = penetration
      self.armor_type = armor_type
      if not (armor_type == const.CHOBHAM or armor_type == const.COMPOSITE or armor_type == const.CERAMIC):
          raise Exception('Invalid armor type %s' % (armor_type))
      self.tanks = []
      self.test = []
          
    def set_name(self, name) -> None:
        """ Set tank name """
        self.name = name
    
    def vulnerable(self, tank) -> bool:
        """ Test if tank is vulnerable to self (armor weaker then penetration) """
        real_armor = self.armor
        if self.armor_type == const.CHOBHAM:
            real_armor += 100
        elif self.armor_type == const.COMPOSITE or self.armor_type == const.CERAMIC:
            real_armor += 50

        if real_armor <= tank.penetration: 
            return True
        return False
    
    def swap_armor(self, othertank: object) -> object:
        """ Swap armour """
        othertank.armor = self.armor
        return othertank