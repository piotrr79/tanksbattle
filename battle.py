import random
import constant as const
from tank import Tank
from tank_calculations import TanksCalculations

class Battle:
    """ Class Battle """

    def __init__(self):
        pass
 
    def __calculate_result(self, attacker, defender, sample_tank) -> str:
        return TanksCalculations(attacker, defender, sample_tank).test_tank_safe()
    
    def __random_armout(self) -> str:
        armour_type = [const.CHOBHAM, const.COMPOSITE, const.CERAMIC]
        random.shuffle(armour_type)
        return armour_type[1]
    
    def play_input(self, attacker: dict, defender: dict, sample_tank: dict) -> str:
        """ Play with user input """
        attackerTank = Tank(attacker['armor'], attacker['penetration'], attacker['armor_type'])
        defenderTank = Tank(defender['armor'], defender['penetration'], defender['armor_type'])
        sampleTank = Tank(sample_tank['armor'], sample_tank['penetration'], sample_tank['armor_type'])
        return Battle.__calculate_result(self, attackerTank, defenderTank, sampleTank)
  
    def play_random(self ) -> str:
        """ Play with random input """
        attackerTank = Tank(random.randrange(400, 700), random.randrange(400, 700), Battle.__random_armout(self))
        defenderTank = Tank(random.randrange(400, 700), random.randrange(400, 700), Battle.__random_armout(self))
        sampleTank = Tank(random.randrange(400, 700), random.randrange(400, 700), Battle.__random_armout(self))
        return Battle.__calculate_result(self, attackerTank, defenderTank, sampleTank)
