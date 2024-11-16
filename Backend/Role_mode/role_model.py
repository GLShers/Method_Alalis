from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Model
from User_mode.user_models import User

class Role(Model):

    __tablename__ = "roles"
    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True, index=True)
    description = Column(String)
    
    users = relationship("User", back_populates="role")
    # Определяем обратную связь с пользователем

