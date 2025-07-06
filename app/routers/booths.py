from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

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