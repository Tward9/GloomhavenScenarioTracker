from datetime import datetime
from app.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, ARRAY
from sqlalchemy.orm import relationship


class Scenario(Base):
    __tablename__ = 'scenarios'
    id = Column(Integer, primary_key=True)
    scenario_name = Column(String(255), nullable=False)
    requirements = Column(ARRAY(Integer),)
    user_id = Column(Integer, ForeignKey('users.id'))
    playthough_id = Column(Integer, ForeignKey('playthroughs.id'))

    user = relationship('User')
