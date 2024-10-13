from sqlalchemy.orm import Session
import pandas as pd
from models.data import engine

def fetch_datetime():
    date_time = pd.read_sql("SELECT datetime FROM trade_data" ,con=engine)
    return date_time

def fetch_close():
    close = pd.read_sql("SELECT close FROM trade_data" ,con=engine)
    return close

def calculate_moving_averages():
    df = fetch_close()
    df['short_mavg'] = df['close'].rolling(window=30, min_periods=1).mean()
    df['long_mavg'] = df['close'].rolling(window=120, min_periods=1).mean()
    return df

def generate_signals(df):
    df['signal'] = 0
    df.loc[df['short_mavg'] > df['long_mavg'], 'signal'] = 1 #buy = 1
    df.loc[df['short_mavg'] < df['long_mavg'], 'signal'] = -1 #sell = -1
    df['short_mavg'] = df['short_mavg'].round(2)
    df['long_mavg'] = df['long_mavg'].round(2)
    # pd.set_option('display.max_rows', None)
    # pd.set_option('display.max_columns', None)
    return df

df = generate_signals(calculate_moving_averages())
