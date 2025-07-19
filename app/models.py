#데이터베이스에 생성될 테이블의 구조 정의

from sqlalchemy import Column, Integer, String, Enum, DECIMAL
from .database import Base
from .schemas import MainCategory, SubCategory, OperatingTime , GroupType


class Booth(Base):
    __tablename__ = "booths"

    group_type = Column(Enum(GroupType), nullable=False)
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    main_category = Column(Enum(MainCategory), nullable=False)
    sub_category = Column(Enum(SubCategory), nullable=False)
    operating_time = Column(Enum(OperatingTime), nullable=False)

    description = Column(String)
    location = Column(String)
    latitude = Column(DECIMAL(9, 6), nullable=False)
    longitude = Column(DECIMAL(10, 7), nullable=False)