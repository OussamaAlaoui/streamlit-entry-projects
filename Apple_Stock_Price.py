
import yfinance as yf
import streamlit as st

st.write("""
# Simple Stock Price App
Shown are the stock closing price and volume of Apple!
""")

tickerSymbol = 'AAPL'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start='2007-5-31', end='2021-12-7')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)