import matplotlib.pyplot as plt

def plot_data(df):
    plt.figure(figsize=(14, 7))
    
    plt.plot(df.index, df['close'], label='Close Price', color='black', linewidth=1.5)
    plt.plot(df.index, df['short_mavg'], label='30-Day Moving Average', color='blue', linewidth=1.5, linestyle='--')
    plt.plot(df.index, df['long_mavg'], label='120-Day Moving Average', color='red',linewidth=1.5, linestyle='--')

    buy_signals = df[df['signal'] == 1]
    sell_signals = df[df['signal'] == -1]
    
    plt.scatter(buy_signals.index, buy_signals['close'], marker='^', color='green', label='Buy Signal', s=40, alpha=0.7)
    plt.scatter(sell_signals.index, sell_signals['close'], marker='v', color='red', label='Sell Signal', s=40, alpha=0.7)
    
    plt.title('Stock Price and Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend(loc='upper left', fontsize='medium')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()