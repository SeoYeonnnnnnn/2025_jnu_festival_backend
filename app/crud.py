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
