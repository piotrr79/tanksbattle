import sys
import os
# Tell syspath where to import modules from other folders in root direcotry
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from armour_py.utils.env import EnvReader
from .base_models import Users, Stats
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import update
import datetime

class GameStatistics():

    def __init__(self): 
        pass
    
    def save_result(self, name, ip, score):
        """ Save result

            Args:
            self: Self.
            score: Score, ip: Ip

            Returns:
                Driver boolean

        """
        engine = create_engine(EnvReader.getDbUrl(self), echo=True)
        Session = sessionmaker(bind=engine)
        session = Session()    
        player =  session.query(Stats).filter(Stats.player_name==name).filter(Stats.player_ip==ip)

        result = ''
        # If not in db save and return player
        if not player:
            updated = datetime.datetime.utcnow
            score = Stats(player_name=name, player_ip=ip, player_score=score, number_of_games=1, last_updated=updated)
            session.add(score)
            session.commit()
            result = score
        else:
            user_score = player.player_score + score
            updated = datetime.datetime.utcnow
            games = player.number_of_games + 1
            result = update(Stats).where(score.uuid==player.uuid).values(player_score =user_score, number_of_games=games, last_updated=updated).execution_options(synchronize_session="fetch")
            session.execute(result)
            session.commit()
        session.close()

        return result
    