import unittest
from datetime import datetime
from models.data import engine
from sqlalchemy.orm import sessionmaker
from models.data_model import TradeData

SessionLocal = sessionmaker(bind=engine, autoflush=False)

class TestValidation(unittest.TestCase):
    def test_data_types(self):
        with SessionLocal() as db:
            data = db.query(TradeData).first()
            if data is None:
                self.fail("No data found in the trade_data table.")

            self.assertIsInstance(data.open, float, "Open should be a float value")
            self.assertIsInstance(data.high, float, "High should be a float value")
            self.assertIsInstance(data.low, float, "Low should be a float value")
            self.assertIsInstance(data.close, float, "Close should be a float value")
            self.assertIsInstance(data.volume, int, "Volume should be an integer value")
            self.assertIsInstance(data.instrument, str, "Instrument should be a string")
            self.assertIsInstance(data.datetime, datetime, "Datetime should be a datetime type")

if __name__ == "__main__":
    unittest.main() 
    
    