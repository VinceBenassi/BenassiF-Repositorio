import streamlit as st
import pandas as pd

st.write("""
#Hola Mundo
""")

df = pd.read_csv("/home/franco/Descargas/Regiones - Hoja 1.csv")
st.line_chart(df)