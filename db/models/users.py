from sqlalchemy import Column, BigInteger, String

from db.base import CleanModel, BaseModel


class Users(CleanModel, BaseModel):
    __tablename__ = 'users'

    user_id  = Column(BigInteger, primary_key=True, unique=True, nullable=False)
    username = Column(String, nullable=True)
    ai_thread_id = Column(String, nullable=True, unique=True)