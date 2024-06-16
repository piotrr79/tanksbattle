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
                Stats result

        """

        print('PR Debug name', name)
        print('PR Debug ip', ip)
        print('PR Debug score', score)

        print('PR Debug db_path', EnvReader.getDbUrl(self))

        engine = create_engine(EnvReader.getDbUrl(self), echo=True)

        print('PR Debug engine', engine)

        Session = sessionmaker(bind=engine)
        session = Session()    
        player =  session.query(Users).filter(Users.player_name == name).filter(Users.player_ip == ip).first()
        session.commit()

        print('PR Debug player', player)

        result = ''
        # If not in db save and return player

        print('PR Debug before if not player case')

        if not player:

            print('PR Debug if not player case')

            updated = datetime.datetime.now()

            print('PR Debug updated', updated)

            user = Users(player_name = name, player_ip = ip, last_updated = updated)

            print('PR Debug user', user)

            session.add(user)
            session.commit()
            score = Stats(user_id = user, player_score = score, number_of_games = 1, last_updated = updated)

            print('PR Debug score', score)

            session.add(score)
            session.commit()
            result = score
        else:
            stats =  session.query(Stats).filter(Stats.user_id == player).first()

            print('PR Debug stats', stats)

            user_score = stats.player_score + score
            updated = datetime.datetime.now()
            games = player.number_of_games + 1
            result = update(Stats).where(stats.user_id==player).values(player_score = user_score, number_of_games=games, last_updated=updated).execution_options(synchronize_session="fetch")
            session.execute(result)
            session.commit()
        session.close()

        return result