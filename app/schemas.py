# API가 요청(Request)을 받거나 응답(Response)을 보낼 때, 데이터의 형태와 유효성을 검사하는 Pydantic 모델

from pydantic import BaseModel

# 부스 생성을 위한 스키마 (ID는 자동 생성되므로 불필요)
class BoothCreate(BaseModel):
    name: str
    category: str
    description: str
    location: str
    latitude: float
    longitude: float


# 부스 정보를 읽기 위한 스키마 (DB의 모든 필드 포함)
class Booth(BoothCreate):
    id: int
    pass

    class Config:
        orm_mode = True # SQLAlchemy 모델과 자동으로 매핑되도록 설정