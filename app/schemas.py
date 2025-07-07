# API가 요청(Request)을 받거나 응답(Response)을 보낼 때, 데이터의 형태와 유효성을 검사하는 Pydantic 모델

from pydantic import BaseModel
from typing import Optional
from enum import Enum

# ✅ 새로운 카테고리 분류를 Enum으로 정의
class BoothCategory(str, Enum):
    BOOTHS_TABLES = "부스 & 테이블존"
    CONTENTS_PHOTO = "콘텐츠 & 포토존"
    PERFORMANCE = "공연 & 관련부스"
    SAFETY = "안전관리"
    ECO = "다회용기 반납"

# 부스 생성을 위한 스키마
class BoothCreate(BaseModel):
    name: str
    category: BoothCategory # category 타입을 새로운 Enum으로 변경
    description: str
    location: str
    latitude: float
    longitude: float

# 부스 수정을 위한 스키마
class BoothUpdate(BaseModel):
    name: Optional[str] = None
    category: Optional[BoothCategory] = None
    description: Optional[str] = None
    location: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None



# 부스 정보를 읽기 위한 스키마 (DB의 모든 필드 포함)
class Booth(BoothCreate):
    id: int
    pass

    class Config:
        orm_mode = True # SQLAlchemy 모델과 자동으로 매핑되도록 설정