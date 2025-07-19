
from sqlalchemy.orm import Session
from typing import List
from fastapi import APIRouter, Depends, HTTPException # HTTPException이 import 되어있는지 확인


from .. import crud, schemas
from ..database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Booth)
def create_new_booth(booth: schemas.BoothCreate, db: Session = Depends(get_db)):
    return crud.create_booth(db=db, booth=booth)

@router.get("/", response_model=List[schemas.Booth])
def read_all_booths(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    booths = crud.get_booths(db, skip=skip, limit=limit)
    return booths

@router.delete("/{booth_id}", response_model=schemas.Booth)
def delete_existing_booth(booth_id: int, db: Session = Depends(get_db)):
    db_booth = crud.delete_booth(db=db, booth_id=booth_id)
    if db_booth is None:
        raise HTTPException(status_code=404, detail="해당 ID의 부스를 찾을 수 없습니다.")
    return db_booth

@router.put("/{booth_id}", response_model=schemas.Booth)
def update_existing_booth(booth_id: int, booth: schemas.BoothUpdate, db: Session = Depends(get_db)):
    db_booth = crud.update_booth(db=db, booth_id=booth_id, booth=booth)
    if db_booth is None:
        raise HTTPException(status_code=404, detail="해당 ID의 부스를 찾을 수 없습니다.")
    return db_booth


@router.get("/", response_model=List[schemas.BoothResponse])
def read_all_booths(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    booths_from_db = crud.get_booths(db, skip=skip, limit=limit)
    
    # ✅ 2. DB에서 받은 데이터를 응답 모델에 맞게 가공
    response_data = []
    for booth in booths_from_db:
        response_data.append(
            schemas.BoothResponse(
                id=booth.id,
                name=booth.name,
                main_category=booth.main_category.name,  # .name으로 Key값(영문)을 가져옴
                sub_category=booth.sub_category.name,    # .name으로 Key값(영문)을 가져옴
                operating_time=booth.operating_time.name,
                description=booth.description,
                location=booth.location,
                latitude=booth.latitude,
                longitude=booth.longitude
            )
        )
    return response_data