from sqlalchemy import create_engine,Integer,Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
DB_URL = "mysql+pymysql://root:2005@localhost/invsto"
engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(engine)