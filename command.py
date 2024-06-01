import sys, json
import constant as const
from validator_class import MyValidatorClass
from battle import Battle

class ExecuteCommand():
    """ ExecuteCommand class """

    def __init__(self):
        self

    def print_output() -> str:
        
        user_input = sys.argv

        """ Validate and return data dict obj """
        data = MyValidatorClass.validate_input(user_input)

        if data == 'random':
            response = Battle.play_random()
        else:
            response = Battle.play_input(data[const.ATTACKER], data[const.DEFENDER], data[const.SAMPLE_TANK])

        return json.dumps(response, indent=2)



x = ExecuteCommand.print_output()
print(x)