from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Model

class User(Model):

    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    login = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    company= Column(Integer, default=None)
    my_company= Column(Integer, default=None)
    role=Column(String, default=None)
    role_id = Column(Integer, ForeignKey('roles.id'))  # Внешний ключ на таблицу roles

    role = relationship("Role", back_populates="users")
    companies = relationship("Company", back_populates="owner_user")