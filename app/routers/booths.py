# routers/booths.py

from sqlalchemy.orm import Session
from typing import List
from fastapi import APIRouter, Depends, HTTPException

from .. import crud, models, schemas
from ..database import get_db

router = APIRouter()

# DB 모델을 응답 모델로 변환하는 헬퍼 함수
def convert_booth_to_response(booth: models.Booth) -> schemas.BoothResponse:
    """SQLAlchemy 모델 객체를 Pydantic 응답 스키마로 변환합니다."""
    return schemas.BoothResponse(
        id=booth.id,
        name=booth.name,
        main_category=booth.main_category.name,
        sub_category=booth.sub_category.name,
        operating_time=booth.operating_time.name,
        description=booth.description,
        location=booth.location,
        latitude=booth.latitude,
        longitude=booth.longitude
    )

@router.post("/", response_model=schemas.BoothResponse)
def create_new_booth(booth: schemas.BoothCreate, db: Session = Depends(get_db)):
    db_booth = crud.create_booth(db=db, booth=booth)
    return convert_booth_to_response(db_booth)

@router.get("/", response_model=List[schemas.BoothResponse])
def read_booths(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    booths_from_db = crud.get_booths(db, skip=skip, limit=limit)
    return [convert_booth_to_response(b) for b in booths_from_db]

@router.get("/{booth_id}", response_model=schemas.BoothResponse)
def read_booth(booth_id: int, db: Session = Depends(get_db)):
    db_booth = crud.get_booth(db=db, booth_id=booth_id)
    if db_booth is None:
        raise HTTPException(status_code=404, detail="해당 ID의 부스를 찾을 수 없습니다.")
    return convert_booth_to_response(db_booth)

@router.put("/{booth_id}", response_model=schemas.BoothResponse)
def update_existing_booth(booth_id: int, booth: schemas.BoothUpdate, db: Session = Depends(get_db)):
    db_booth = crud.update_booth(db=db, booth_id=booth_id, booth=booth)
    if db_booth is None:
        raise HTTPException(status_code=404, detail="해당 ID의 부스를 찾을 수 없습니다.")
    return convert_booth_to_response(db_booth)

@router.delete("/{booth_id}", response_model=schemas.BoothResponse)
def delete_existing_booth(booth_id: int, db: Session = Depends(get_db)):
    db_booth = crud.delete_booth(db=db, booth_id=booth_id)
    if db_booth is None:
        raise HTTPException(status_code=404, detail="해당 ID의 부스를 찾을 수 없습니다.")
    return convert_booth_to_response(db_booth)