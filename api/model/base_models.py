from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, DeclarativeBase
import datetime
import uuid

class Base(DeclarativeBase):
    """ Class Base """

class Users(Base):
    """ Class Users 
        ToDo - Implement user authorisation
    """
    __tablename__ = 'Users'
    uuid = Column('uuid', String(36), primary_key=True, default=str(uuid.uuid4()))
    player_name = Column('player_name', String(255))
    player_ip = Column('player_ip', String(255))
    created = Column('created', DateTime, default=datetime.datetime.now())
    last_updated = Column('last_updated', DateTime)
    stats = relationship("Stats")

class Stats(Base):
    """ Class Stats """
    __tablename__ = 'Stats'
    uuid = Column('uuid', String(36), primary_key=True, default=str(uuid.uuid4()))
    user_id = Column(String(36), ForeignKey('Users.uuid'))
    player_score = Column('player_score', Integer())
    number_of_games = Column('number_of_games', Integer())
    created = Column('created', DateTime, default=datetime.datetime.now())
    last_updated = Column('last_updated', DateTime)
