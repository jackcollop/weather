import pandas as pd
import streamlit as st
import plotly.express as px

r = pd.read_csv(r'rain.csv', header=None)

r.set_index(0, inplace=True)

r.columns= range(1980,2026)

fig = px.funnel(r)

st.subheader('TX cotton acre-weighted cumulative precipitation (in.)')

st.plotly_chart(fig)
