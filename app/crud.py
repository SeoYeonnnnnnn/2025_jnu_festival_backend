#데이터베이스에 데이터를 읽고 쓰는 함수

from sqlalchemy.orm import Session
from . import models, schemas

# 특정 부스 정보 가져오기
def get_booth(db: Session, booth_id: int):
    return db.query(models.Booth).filter(models.Booth.id == booth_id).first()

# 모든 부스 목록 가져오기
def get_booths(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Booth).offset(skip).limit(limit).all()

# 부스 정보 생성하기
def create_booth(db: Session, booth: schemas.BoothCreate):
    db_booth = models.Booth(**booth.dict())
    db.add(db_booth)
    db.commit()
    db.refresh(db_booth)
    return db_booth
    

def delete_booth(db: Session, booth_id: int):
    db_booth = db.query(models.Booth).filter(models.Booth.id == booth_id).first()
    if db_booth:
        db.delete(db_booth)
        db.commit()
    return db_booth

def update_booth(db: Session, booth_id: int, booth: schemas.BoothUpdate):
    # 1. DB에서 해당 ID의 부스를 찾습니다.
    db_booth = db.query(models.Booth).filter(models.Booth.id == booth_id).first()

    if db_booth:
        # 2. Pydantic 모델로부터 받은 데이터를 딕셔너리로 변환합니다.
        # exclude_unset=True는 사용자가 값을 보낸 필드만 업데이트하기 위함입니다.
        update_data = booth.dict(exclude_unset=True)
        
        # 3. 딕셔너리의 각 항목에 대해 DB 모델의 속성을 업데이트합니다.
        for key, value in update_data.items():
            setattr(db_booth, key, value)
            
        db.commit()
        db.refresh(db_booth)
        
    return db_booth