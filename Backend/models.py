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
    
    


    # Определяем связь с компаниями

    companies = relationship("Company", back_populates="owner_user")


class Company(Model):

    __tablename__ = "company"
    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True, index=True)
    description = Column(String)
    owner_user_id = Column(Integer, ForeignKey("users.id"))
    # Определяем обратную связь с пользователем

    owner_user = relationship("User", back_populates="companies")
