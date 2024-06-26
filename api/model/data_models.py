import sys
import os
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
    
    def save_result(self, name: str, ip: str, score: int) -> object:
        """ Save result

            Args:
            self: Self.
            score: Score, ip: Ip

            Returns:
                Stats result

        """
        engine = create_engine(EnvReader.get_db_url(self), echo=True)

        Session = sessionmaker(bind=engine)
        session = Session()    
        player =  session.query(Users).filter(Users.player_name == name).filter(Users.player_ip == ip).first()

        result = ''
        # If not in db save and return player
        if not player:
            updated = datetime.datetime.now()
            user = Users(player_name = name, player_ip = ip, last_updated = updated)
            session.add(user)
            session.commit()
            score = Stats(user_id = user.uuid, player_score = score, number_of_games = 1, last_updated = updated)
            session.add(score)
            session.commit()
            player = score
        else:
            stats =  session.query(Stats).filter(Stats.user_id == player.uuid).first()
            if not stats:
                updated = datetime.datetime.now()
                score = Stats(user_id = player.uuid, player_score = score, number_of_games = 1, last_updated = updated)
                session.add(score)
                session.commit()
            else:
                user_score = stats.player_score + score
                updated = datetime.datetime.now()
                games = stats.number_of_games + 1
                statement = update(Stats).where(Stats.uuid == stats.uuid).values(player_score = user_score, number_of_games = games, last_updated = updated).execution_options(synchronize_session="fetch")
                session.execute(statement)
                session.commit()

        result =  session.query(Stats).filter(Stats.user_id==player.uuid).first()
        session.close()

        return result