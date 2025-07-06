
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