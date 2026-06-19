from sqlalchemy import Column, Integer, String

from app.database import Base


class PlayerProfile(Base):
    __tablename__ = "player_profiles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    handicap = Column(Integer, nullable=False)
    driver_distance = Column(Integer, nullable=False)
    seven_iron_distance = Column(Integer, nullable=False)
    common_miss = Column(String, nullable=False)
    current_focus = Column(String, nullable=False)