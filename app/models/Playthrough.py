from email.policy import default
from app.db import Base
from .Scenario import Scenario
from .Achievements import Achievement
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, ARRAY, select, func
from sqlalchemy.orm import relationship, column_property


class Playthrough(Base):
    __tablename__ = 'playthroughs'
    id = Column(Integer, primary_key=True)
    players = Column(String(255), nullable=False)
    unlocked_scenarios = Column(ARRAY(Integer))
    completed_scenarios = Column(ARRAY(Integer))
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User')
    scenarios = relationship('Scenario',)
    achievements = relationship('Achievement')

