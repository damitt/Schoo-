from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import scores, models, schemas
from ..database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/scores/", response_model=schemas.Score)
def create_score(score: schemas.ScoreCreate, db: Session = Depends(get_db)):
    return scores.create_score(db=db, score=score)

@router.get("/scores/{score_id}", response_model=schemas.Score)
def read_score(score_id: int, db: Session = Depends(get_db)):
    db_score = scores.get_score(db, score_id=score_id)
    if db_score is None:
        raise HTTPException(status_code=404, detail="Score not found")
    return db_score

@router.patch("/scores/{score_id}", response_model=schemas.Score)
def update_score(score_id: int, score: schemas.ScoreCreate, db: Session = Depends(get_db)):
    db_score = scores.update_score(db=db, score_id=score_id, score=score)
    if db_score is None:
        raise HTTPException(status_code=404, detail="Score not found")
    return db_score

@router.delete("/scores/{score_id}", response_model=schemas.Score)
def delete_score(score_id: int, db: Session = Depends(get_db)):
    db_score = scores.delete_score(db=db, score_id=score_id)
    if db_score is None:
        raise HTTPException(status_code=404, detail="Score not found")
    return db_score
