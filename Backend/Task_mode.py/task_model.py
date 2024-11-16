from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Model
from User_mode.user_models import User

class Company(Model):

    __tablename__ = "company"
    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True, index=True)
    description = Column(String)
    owner_user_id = Column(Integer, ForeignKey("users.id"))
    # Определяем обратную связь с пользователем

    owner_user = relationship("User", back_populates="companies")
