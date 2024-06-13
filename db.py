# https://download.sqlitebrowser.org/DB.Browser.for.SQLite-3.12.2-win64.msi

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
engine = create_engine("sqlite:///baza.db")
Session = sessionmaker(bind=engine)
sesija = Session()
Base = declarative_base()
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    email = Column(String)
Base.metadata.create_all(engine)