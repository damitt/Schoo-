from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

from .config import cfg


class Student(Base):
    __tablename__ = cfg.cfg["db"]["tables"]["students"]

    print(__tablename__)

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    scores = relationship("Score", back_populates="student")


class Score(Base):
    __tablename__ = cfg.cfg["db"]["tables"]["scores"]

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    score = Column(Integer)

    student = relationship("Student", back_populates="scores")
