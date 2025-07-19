from pydantic import BaseModel
from typing import Optional
from enum import Enum

# 1. 대분류 Enum 정의 (가장 큰 카테고리)
class MainCategory(str, Enum):
    PERFORMANCE = "공연 구역"
    BOOTH = "부스 구역"
    EXPERIENCE = "체험 구역"
    FNB = "F&B 구역"
    SUPPORT = "운영 및 지원 구역"
    FACILITIES = "편의시설" 

class GroupType(str, Enum):
    MAJOR = "대분류"
    SUB = "소분류"

# 2. 소분류 Enum 정의 (각 대분류에 속하는 세부 항목)
class SubCategory(str, Enum):
    # 공연 구역
    MAIN_STAGE = "본무대"
    STREET_KARAOKE = "거리노래방"
    
    # 부스 구역
    STUDENT_BOOTH = "학생부스"
    COMPANY_BOOTH = "기업부스"
    COMMERCIAL_BOOTH = "상권부스"
    POPUP_STORE = "팝업스토어"

    # 체험 구역
    CONTENTS_ZONE = "컨텐츠존"
    PHOTO_ZONE = "포토존"
    PHOTO_BOOTH = "영수증사진기 & 전대네컷"
    
    # F&B 구역
    FOOD_TRUCK = "푸드트럭"
    TABLE_ZONE = "테이블존"
    
    # 운영 및 지원 구역
    WRISTBAND_BOOTH = "전대존 팔찌 배부 부스"
    SAFETY_BOOTH = "안전관리부스"
    REUSABLE_CONTAINER_BOOTH = "다회용기 반납부스"

    RESTROOM = "화장실"
    TRASH_CAN = "쓰레기통"
    SMOKING_AREA = "흡연장"


    MAJOR_CATEGORY = "대분류"


# 운영 시간 분류를 위한 Enum
class OperatingTime(str, Enum):
    DAY = "낮 운영"
    NIGHT = "밤 운영"
    ALL_DAY = "상시 운영"


# 3. 새로운 Enum을 적용한 Pydantic 스키마
# 부스 생성을 위한 스키마
class BoothCreate(BaseModel):
    group_type: GroupType
    name: str
    main_category: MainCategory
    sub_category: SubCategory
    operating_time: OperatingTime  # ✅ 운영 시간 필드 추가
    description: str
    location: str
    latitude: float
    longitude: float

# 부스 수정을 위한 스키마
class BoothUpdate(BaseModel):
    group_type: Optional[GroupType] = None
    name: Optional[str] = None
    main_category: Optional[MainCategory] = None
    sub_category: Optional[SubCategory] = None
    operating_time: Optional[OperatingTime] = None  # ✅ 운영 시간 필드 추가
    description: Optional[str] = None
    location: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None

# 부스 정보를 읽기 위한 스키마
class Booth(BoothCreate):
    id: int
    
    class Config:
        orm_mode = True

class BoothResponse(BaseModel):
    id: int
    name: str
    main_category: str  # Enum이 아닌 일반 str로 변경
    sub_category: str   # Enum이 아닌 일반 str로 변경
    operating_time: str # Enum이 아닌 일반 str로 변경
    description: str
    location: str
    latitude: float
    longitude: float

    class Config:
        orm_mode = True