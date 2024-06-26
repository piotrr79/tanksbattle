import sys
import os
import pytest
# Tell syspath where to import modules from other folders in root direcotry
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import utils.constant as const
from tanksbattle.battle import Battle

class TestArmour():

    def test_tank_safe(self):
        """ Test for tank safe case """
        attacker = {const.ARMOUR : 600, const.PENETRATION : 670, const.ARMOUR_TYPE : const.CHOBHAM}
        defender = {const.ARMOUR : 620, const.PENETRATION : 670, const.ARMOUR_TYPE : const.CHOBHAM}
        sample_tank = {const.ARMOUR : 400, const.PENETRATION : 400, const.ARMOUR_TYPE : const.CERAMIC}
        result = Battle.play_input(self, attacker, defender, sample_tank)
        assert result == const.TANK_IS_SAFE

    def test_tank_not_safe(self):
        """ Test for tank not safe case """
        attacker = {const.ARMOUR : 620, const.PENETRATION : 670, const.ARMOUR_TYPE : const.CHOBHAM}
        defender = {const.ARMOUR : 600, const.PENETRATION : 670, const.ARMOUR_TYPE : const.CHOBHAM}
        sample_tank = {const.ARMOUR : 800, const.PENETRATION : 400, const.ARMOUR_TYPE : const.CERAMIC}
        result = Battle.play_input(self, attacker, defender, sample_tank)
        assert result == const.NO_TANK_IS_SAFE

    def test_tank_vulnerable_to_self(self):
        """ Test for vulnerable to self case """
        attacker = {const.ARMOUR : 120, const.PENETRATION : 1670, const.ARMOUR_TYPE : const.CHOBHAM}
        defender = {const.ARMOUR : 120, const.PENETRATION : 1670, const.ARMOUR_TYPE : const.CHOBHAM}
        sample_tank = {const.ARMOUR : 400, const.PENETRATION : 400, const.ARMOUR_TYPE : const.CERAMIC}
        result = Battle.play_input(self, attacker, defender, sample_tank)
        assert result == const.VULNERABLE_TO_SELF

    def test_tank_invalid_armour(self):
        """ Test for invalid armour case """
        attacker = {const.ARMOUR : 620, const.PENETRATION : 970, const.ARMOUR_TYPE : const.CHOBHAM}
        defender = {const.ARMOUR : 600, const.PENETRATION : 1670, const.ARMOUR_TYPE : const.CHOBHAM}
        sample_tank = {const.ARMOUR : 400, const.PENETRATION : 400, const.ARMOUR_TYPE : 'fake_amror'}
        with pytest.raises(Exception):
            Battle.play_input(self, attacker, defender, sample_tank)

if __name__ == '__main__':
    pytest.main()