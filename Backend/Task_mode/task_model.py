from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, TIMESTAMP 
from sqlalchemy.orm import relationship
from database import Model
from User_mode.user_models import User

class Task(Model):

    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    name_task = Column(String, index=True)
    descr_task = Column(String, default=None)
    date=Column(TIMESTAMP, index=True)
    state= Column(Integer, default=1, index=True)
    owner_user_id = Column(Integer, ForeignKey("users.id"))
    # Определяем обратную связь с пользователем

    owner_user = relationship("User", back_populates="task")
