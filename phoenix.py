$ pip install streamlit
import streamlit as st
import pandas as pd
 
st.write("""
# My first app
Hello *world!*
""")
 
df = pd.read_csv("https://github.com/aumhope/3030hope/blob/main/business-operations-survey-2022-information-and-communications-technology.csv")
st.line_chart(df)
