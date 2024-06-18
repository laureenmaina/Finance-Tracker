from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from finance import Base  # Assuming Base is defined in functions.py

engine = create_engine('sqlite:///finance.db')
Base.metadata.drop_all(engine)  # Drop all existing tables
Base.metadata.create_all(engine)  # Create tables based on current models

