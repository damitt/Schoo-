from sqlalchemy.orm import Session
from . import models, schemas

def get_score(db: Session, score_id: int):
    return db.query(models.Score).filter(models.Score.id == score_id).first()

def create_score(db: Session, score: schemas.ScoreCreate):
    db_score = models.Score(**score.dict())
    db.add(db_score)
    db.commit()
    db.refresh(db_score)
    return db_score

def update_score(db: Session, score_id: int, score: schemas.ScoreCreate):
    db_score = get_score(db, score_id)
    if db_score:
        for key, value in score.dict().items():
            setattr(db_score, key, value)
        db.commit()
        db.refresh(db_score)
    return db_score

def delete_score(db: Session, score_id: int):
    db_score = get_score(db, score_id)
    if db_score:
        db.delete(db_score)
        db.commit()
    return db_score
