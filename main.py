import yfinance as yf
import pandas as pd

dataF = yf.download("EURUSD=X", start="2023-11-6", end="2023-11-11", interval="15m")
dataF.iloc[:,:]
dataF.Open.iloc

def signal_generator(df):
    open = df.Open.iloc[-1]
    close = df.Close.iloc[-1]
    previous_open = df.Open.iloc[-2]
    previous_close = df.Close.iloc[-2]

    # Bearish Pattern
    if (open>close and
    previous_open<previous_close and
    close<previous_open and
    open>=previous_close):
        return 1

    # Bullish Pattern
    elif (open < close and
            previous_open > previous_close and
            close > previous_open and
            open <= previous_close):
        return 2

    #no clear pattern
    else:
        return 0

signal = []
signal.append(0)
for i in range(1,len(dataF)):
    df = dataF[i-1:i+1]
    signal.append(signal_generator(df))

#signal_generator(data)
dataF["signal"] = signal

#data value count
dataF.iloc[:, :]

