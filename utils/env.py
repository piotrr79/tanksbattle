import sys
import os
# Tell syspath where to import modules from other folders in root direcotry
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from decouple import config

class EnvReader():
    """ Get runtime params from env """

    def __init__(self):
        pass

    @staticmethod
    def get_traceback_limit():
        """ Get traceback limit 

            Returns:
                limit string
        """
        if os.environ.get('TRACEBACK_LIMIT_ENV') is not None:   
            value = os.environ['TRACEBACK_LIMIT_ENV']
        else:
            value = config('TRACEBACK_LIMIT_ENV')
        
        return value
    
    def get_db_url(self):
        """ Get db url

            Returns:
                Db url string
        """
        if os.environ.get('DB_URL') is not None:   
            dburl = os.environ['DB_URL']
        else:
            dburl = config('DB_URL')
        
        return dburl
    
    def get_token_server_endpoint(self):
        """ Get token server endpoint

            Returns:
                Token server url string
        """
        if os.environ.get('TOKEN_SERVER') is not None:   
            endpoint = os.environ['TOKEN_SERVER']
        else:
            endpoint = config('TOKEN_SERVER')
        
        return endpoint

