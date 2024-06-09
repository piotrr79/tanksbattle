import sys, json
import utils.constant as const
from utils.validator_class import MyValidatorClass
from tanksbattle.battle import Battle

class ExecuteCommand():
    """ ExecuteCommand class """

    def __init__(self):
        pass

    def print_output(self) -> str:
        
        user_input = sys.argv

        # Validate and return data dict obj
        data = MyValidatorClass.validate_input(self, user_input)

        if data == 'random':
            response = Battle.play_random(self)
        else:
            response = Battle.play_input(self, data[const.ATTACKER], data[const.DEFENDER], data[const.SAMPLE_TANK])

        return json.dumps(response, indent=2)



x = ExecuteCommand.print_output(ExecuteCommand)
print(x)
