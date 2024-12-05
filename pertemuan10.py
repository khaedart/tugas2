import pandas as pd
import streamlit as st
import plotly.express as px
import yfinance as yf

st.title("Pertemuan 10: Interaksi Streamlit dan Yahoo finance")
st.write("# Pendahuluan")

kamus_ticker = {
    'GOOGL':'Google',
    'AAPL':'Apple',
    'SBUX':'Starbucks',
    'MCD':'McDonalds',
    'BBNI':'Bank Negara Indonesia (persero) Tbk PT'
    
    
}
tickerSymbol = st.selectbox(
    'Silakan pilih kode perusahaan:',
    kamus_ticker.keys()
)


st.write(f'{kamus_ticker.keys()}')
st.write(f'Harga saham {kamus_ticker[tickerSymbol]}.')

tickerData = yf.Ticker(tickerSymbol)
pilihan_periode = st.selectbox(
    'Pilih priode:',
    ['1d','5d','1mo','3mo','6mo','1y','2y']
)
tickerDF = tickerData.history(
    period='1d',
    start='2024-10-01',
    end='2024-11-06'
)
flag_tampil = st.checkbox('Tampilkan tabel')
if flag_tampil:
    st.write(tickerDF.head(10))
    
flag_grafik = st.checkbox('Tampilkan grafik')   
pilihan_atribut = st.multiselect(
        'silakan pilih atribut yang akan di tampilakan:',
        ['Low', 'High', 'Open', 'Close', 'Volume']
)
grafik =px.line(
    tickerDF,
    title=f'Harga Saham {tickerSymbol}',
    y = pilihan_atribut
        
)
st.plotly_chart(grafik)

        
