import streamlit as st
import pandas as pd

st.title("GitHub Pages + Streamlit Test")
st.write("If you see this, stlite is running in your browser!")

df = pd.DataFrame({
    "Column A": ["A", "B", "C"],
    "Column B": [10, 20, 30]
    })
st.dataframe(df)
