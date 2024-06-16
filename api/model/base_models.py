import sys
import os
# Tell syspath where to import modules from other folders in root direcotry
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from utils.env import EnvReader

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, DeclarativeBase
import datetime
import uuid

class Base(DeclarativeBase):
    """ Class Base """
    pass

class Users(Base):
    """ Class Users """
    __tablename__ = 'users'
    uuid = Column('uuid', String(36), primary_key=True, default=uuid.uuid4)
    player_name = Column('player_name', String(255))
    created = Column('created', DateTime, default=datetime.datetime.now())
    last_updated = Column('last_updated', DateTime)
    comments = relationship("Stats")

class Stats(Base):
    """ Class Stats """
    __tablename__ = 'stats'
    uuid = Column('uuid', String(36), primary_key=True, default=uuid.uuid4)
    user_id = Column(String(36), ForeignKey('users.uuid'))
    player_name = Column('player_name', String(255))
    player_ip = Column('player_ip', String(255))
    player_score = Column('player_score', Integer())
    number_of_games = Column('number_of_games', Integer())
    created = Column('created', DateTime, default=datetime.datetime.now())
    last_updated = Column('last_updated', DateTime)
