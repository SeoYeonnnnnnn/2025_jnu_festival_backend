#데이터베이스에 생성될 테이블의 구조 정의

from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Booth(Base):
    __tablename__ = "booths"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    category = Column(String)
    description = Column(String)
    location = Column(String)
    latitude = Column(Float)  # 위도
    longitude = Column(Float) # 경도