#pip install sqlalchemy

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey  # connnection to the database
from sqlalchemy.orm import sessionmaker, declarative_base, relationship # connection
#from sqlalchemy.ext.declarative import declarative_base

# username:password@host/database
engine = create_engine("mssql+pymssql://dbadmin:Qwerty123@smx2024.database.windows.net:1433/dataAnalytics") 
# username, password, host, za koja baza stanuva zbor
# // me,a potreba da se specifira deka abazata se krira vo istiot folder
# so koja baza ke se povrzeme i kade taa baza se naogja
# // oddeluvanje /// deka sakame da bide vo istiot folder
# otvaras konekcija, rabota, zatvoranje na baza
Session = sessionmaker(bind=engine)
sesija = Session() # ja povikuvame sesijata
Base = declarative_base()
# F5 startuvame programa, zastanuva i ja analizirame programata


class User(Base): # site koloni gi redime 
    __tablename__ = 'users_beti' # ime samo za vo python
    
    id = Column(Integer, primary_key = True)
    name = Column(String)
    age = Column(Integer)
    email = Column(String)

        
class Employee(Base):
    __tablename__ = 'employees_Beti' # ime vo SQL baza
    id = Column(Integer, primary_key=True)
    full_name = Column(String)
    email = Column(String)
    age = Column(Integer)
    position =Column(String)
    salary = Column(Integer)
    years_in_company = Column(Integer)
    
class Product(Base):
    __tablename__ = "product_beti"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    
class Sale(Base):  # relacija 
    __tablename__ = "sales_beti"
    id = Column(Integer, primary_key=True)
    employee_id = Column(ForeignKey("employees_Beti.id"))
    product_id = Column(ForeignKey("product_beti.id"))
    
    employee = relationship(Employee)
    product = relationship(Product)
    

Base.metadata.create_all(engine)    
# izvrsuvanje na tabela(create all), se kreiraat ako ne postoele, ako postojat taa tabela nema da se formirada se kreira    
    
    
 

