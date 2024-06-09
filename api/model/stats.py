import sys
import os
# Tell syspath where to import modules from other folders in root direcotry
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from utils.env import EnvReader

from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import update
import datetime
import uuid

Base = declarative_base()

class Stats(Base):
    __tablename__ = 'stats'
    uuid = Column('uuid', String(36), primary_key=True, default=uuid.uuid4)
    player_name = Column('player_name', String(255))
    player_ip = Column('player_ip', String(255))
    player_score = Column('player_score', Integer(10,2))
    number_of_games = Column('number_of_games', Integer(10,2))
    created = Column('created', DateTime, default=datetime.datetime.utcnow)
    last_updated = Column('last_updated', DateTime)

class GameStatistics():

    def __init__(self): 
        self
    
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
    