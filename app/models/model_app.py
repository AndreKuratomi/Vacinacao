from app.configs.database import db
from sqlalchemy import Column, DateTime, String
from dataclasses import dataclass
from datetime import datetime, timedelta

first = datetime.now()
second = first + timedelta(days=90)


@dataclass
class Cards(db.Model):
    cpf: str
    name: str
    first_shot_date: datetime
    second_shot_date: datetime
    vaccine_name: str
    health_unit_name: str

    __tablename__ = "vaccine_cards"

    cpf = Column(String(length=11), primary_key=True, unique=True)
    name = Column(String, nullable=False)
    first_shot_date = Column(DateTime(), default=first)
    second_shot_date = Column(DateTime(), default=second)
    vaccine_name = Column(String, nullable=False)
    health_unit_name = Column(String)
