from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
db_password = os.getenv('DB_PASSWORD')

Base = declarative_base()
DB_URL = f"mysql+pymysql://root:{db_password}@localhost/invsto"
engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(engine)
    
def load_data_to_db(file_path):
    try :
        df = pd.read_excel(file_path)
        df.to_sql('trade_data',con=engine,if_exists='replace',index=False)
        print("Data is inserted successfully")
    except Exception as e:
        print("Error while loading data to db: ",e)

