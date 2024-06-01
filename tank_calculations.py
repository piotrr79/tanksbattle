import sys
import constant as const
import configs
sys.tracebacklimit = configs.TRACEBACK_LIMNIT

""" Class TanksCalculations """
class TanksCalculations:
    def __init__(self, attacker: object, defender: object, sample_tank: object):
        self.tanks = []
        self.test = []
        self.attacker = attacker
        self.defender = defender
        self.sample_tank = sample_tank    
        
    def tanks_computing(self) -> None:
        if self.attacker.vulnerable(self.defender) is True:
            raise Exception(const.VULNERABLE_TO_SELF)
        self.attacker.swap_armor(self.defender)

        for i in range(5):
            self.tanks.append(self.sample_tank)
        
        index = 0
        for tank in self.tanks:
            tank.set_name('Tank' + str(index) + "_Small")
            index += 1

        index = 0
        while index < len(self.tanks):
            self.test.append(self.tanks[i].vulnerable(self.attacker))
            index += 1

    def test_tank_safe(self) -> str:
        at_least_one_safe = False

        self.tanks_computing()
        for t in self.test:
            if t:
                at_least_one_safe = True
        if at_least_one_safe:
            response = const.TANK_IS_SAFE
        else:
            response = const.NO_TANK_IS_SAFE
        
        return response