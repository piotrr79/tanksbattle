import json
from typing import List
import constant as const

class MyValidatorClass:
    """ Validator class """

    def __init__(self):
        self

    def validate_input(arguments: List[str]) -> str:

        """ Validate input

            Args:
            arguments: dict[dict].

            Returns:
                NoReturn
        """

        """ Test if input is not empty """
        if len(arguments) == 1:
            raise Exception(const.INPUT_EMPTY)

        """ Get input from string """
        data_string = arguments[1]

        if data_string == 'random':
            return data_string
        else:
            """ Serialise input string to object """
            data = json.loads(data_string)

            """ Test all required params """
            try:
                data[const.ATTACKER]
                data[const.ATTACKER][const.ARMOUR]
                data[const.ATTACKER][const.PENETRATION]
                data[const.ATTACKER][const.ARMOUR_TYPE]
            except:
                raise Exception(const.PROVIDE_ATT_PARAMS)
            
            try:
                data[const.DEFENDER]
                data[const.DEFENDER][const.ARMOUR]
                data[const.DEFENDER][const.PENETRATION]
                data[const.DEFENDER][const.ARMOUR_TYPE]
            except:
                raise Exception(const.PROVIDE_DEF_PARAMS)
            
            try:
                data[const.SAMPLE_TANK]
                data[const.SAMPLE_TANK][const.ARMOUR]
                data[const.SAMPLE_TANK][const.PENETRATION]
                data[const.SAMPLE_TANK][const.ARMOUR_TYPE]
            except:
                raise Exception(const.PROVIDE_ST_PARAMS)
        
        return data
        