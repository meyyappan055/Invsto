from models.analysis import df
import pandas as pd

def testing_strategy(df,capital):
    shares = 0
    df['portfolio'] = 0
    for i in range(len(df)):
        if df['signal'].iloc[i] == 1:
            if shares == 0:
                shares = capital/df['close'].iloc[i]
                capital = 0
        elif df['signal'].iloc[i] == -1:
            if shares > 0:
                capital = shares*df['close'].iloc[i]
                shares = 0
        df.at[i,'portfolio'] = shares*df['close'].iloc[i] + capital

    df['portfolio'] = df['portfolio'].astype(float).round(2)
    return df
    