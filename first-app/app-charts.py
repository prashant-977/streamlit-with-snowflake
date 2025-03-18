import pandas as pd
import streamlit as st
import plotly.graph_objects as go

st.title('Hierarchical Data Visualization')

df = pd.read_csv('data/employees.csv')

labels = df[df.columns[0]]
parents = df[df.columns[1]]

data = go.Treemap(
    ids=labels,
    labels=labels,
    parents=parents,
    root_color='lightgrey'
)

fig=go.Figure(data)

st.plotly_chart(fig, use_container_width=True)