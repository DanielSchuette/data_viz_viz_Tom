import os
import streamlit as st
import pandas as pd


st.header("Barley Visualization & Analysis")
data: pd.DataFrame = pd.read_csv("./data/barley_data.csv")
st.dataframe(data)
