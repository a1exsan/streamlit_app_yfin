import streamlit as st
import pandas as pd
import yfinance as yf
from bokeh.plotting import figure

st.title('Stocks Prices yFinance:')

@st.cache
def load_data(ticker, start='2015-01-01', end='2021-12-01'):
    data = yf.download(ticker, start=start, end=end)
    data = data.reset_index()
    return data

#col1 = st.columns(1)

tick = st.sidebar.selectbox(
    "Select a company ticker",
    ("GOOG", "TSLA", "NVDA"))

start_date = st.sidebar.date_input("Start Date", pd.to_datetime('2015-01-01').date())
end_date = st.sidebar.date_input("End Date", pd.to_datetime('2021-12-01').date())


ticker = load_data(tick, start=start_date, end=end_date)


if st.checkbox(f'Show line chart {tick}'):

        st.subheader(f'{tick} stock chart:')

        p = figure(
            title='Stock line chart',
            x_axis_label='Date',
            y_axis_label='Close')
        p.line(ticker['Date'], ticker['Close'], legend_label='Price', line_width=2)

        st.bokeh_chart(p, use_container_width=True)

else:
        st.subheader(f'{tick} stocks:')
        st.dataframe(ticker)
