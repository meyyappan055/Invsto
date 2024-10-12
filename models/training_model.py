from sqlalchemy import Column, Integer, String, Date,Float
from models.data import Base

class TradeData(Base):
    __tablename__ = "trade_data"
    id = Column(Integer,primary_key=True,autoincrement=True)
    date= Column(Date,nullable=False)
    close_price = Column(Float,nullable=False)
    high_price = Column(Float,nullable=False)
    low_price = Column(Float,nullable=False)
    open_price = Column(Float,nullable=False)
    volume = Column(Integer,nullable=False)
    instrument = Column(String(30),nullable=False)
