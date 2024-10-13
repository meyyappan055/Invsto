from sqlalchemy import Column, Float, BigInteger, String, DateTime, Text,Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TradeData(Base):
    __tablename__ = 'trade_data'
    id = Column(Integer, primary_key=True)
    open = Column(Float, nullable=True)  
    high = Column(Float, nullable=True)  
    low = Column(Float, nullable=True)   
    close = Column(Float, nullable=True) 
    volume = Column(BigInteger, nullable=True)  
    instrument = Column(Text, nullable=True)  
    datetime = Column(DateTime, nullable=True)  