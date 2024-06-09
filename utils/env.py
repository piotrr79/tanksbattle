import sys
import os
from dotenv import load_dotenv
# Tell syspath where to import modules from other folders in root direcotry
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from decouple import config

class EnvReader():
    """ Get runtime params from env """

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
    
    def getDbUrl(self):
        """ Get db url

            Returns:
                Db url string
        """
        if os.environ.get('DB_URL') is not None:   
            self.dburl = os.environ['DB_URL']
        else:
            self.dburl = config('DB_URL')
        
        return self.dburl

