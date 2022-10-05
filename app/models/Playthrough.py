from email.policy import default
from app.db import Base
from .Scenario import Scenario
from .Achievements import Achievement
from sqlalchemy import Column, Integer, String, ForeignKey, select, func
from sqlalchemy.orm import relationship, column_property


class Playthrough(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User')
    scenarios = relationship('Scenario',)
    achievements = relationship('Achievement')

