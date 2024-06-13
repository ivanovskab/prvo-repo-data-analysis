# pri izvrsuvanje otvarame, potoa ja zatvarame tabelata
from sqlalchemy import create_engine, Column, Integer, String  # connnection to the database
from sqlalchemy.orm import sessionmaker, declarative_base # connection

from database import sesija, User # folder location kade se naogja filelot

user1 = User(name="Bet", age=31, email='iii@gmail.com')
sesija.add(user1)
sesija.commit() # save the change