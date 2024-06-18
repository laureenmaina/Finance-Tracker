from sqlalchemy import create_engine, Column, Integer,Date, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

DATABASE_URI = "sqlite:///finance.db"
engine = create_engine(DATABASE_URI, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    expenses = relationship("Expense", back_populates="user", cascade="all, delete-orphan")
    incomes = relationship("Income", back_populates="user", cascade="all, delete-orphan")
    saving_goals = relationship("SavingGoal", back_populates="user", cascade="all, delete-orphan")

class Expense(Base):
    __tablename__ = 'expenses'
    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    description = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship("User", back_populates="expenses")

class Income(Base):
    __tablename__ = 'incomes'
    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    source = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship("User", back_populates="incomes")

class SavingGoal(Base):
    __tablename__ = 'saving_goals'
    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    target_date = Column(Date, nullable=False)
    description = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship("User", back_populates="saving_goals")


Base.metadata.create_all(engine)
