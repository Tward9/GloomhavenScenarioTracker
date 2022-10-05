from app.db import Base
from .Achievements import Achievement
from sqlalchemy import Column, Integer, String, ForeignKey, select, func
from sqlalchemy.orm import relationship, column_property

class Achievement(Base):
    __tablename__ = 'achievements'
    id = Column(Integer, primary_key=True)
    achievement_title = Column(String(100), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    playthrough_id = Column(Integer, ForeignKey('playthoughs.id'))
    