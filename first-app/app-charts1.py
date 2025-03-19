import pandas as pd
import streamlit as st
import plotly.graph_objects as go

st.title('Hierarchical Data Visualization')

df = pd.read_csv('data/employees.csv')

labels = df[df.columns[0]]
parents = df[df.columns[1]]

def makeTreemap(labels, parents):
    data = go.Treemap(
        ids=labels,
        labels=labels,
        parents=parents,
        root_color='lightgrey'
    )
    fig=go.Figure(data)
    return fig

def makeIcicle(labels, parents):
    data = go.Icicle(
        ids=labels,
        labels=labels,
        parents=parents,
        root_color='lightgrey'
    )
    fig=go.Figure(data)
    return fig  

def makeSunburst(labels, parents):
    data = go.Sunburst(
        ids=labels,
        labels=labels,
        parents=parents,
        root_color='lightgrey'
    )
    fig=go.Figure(data)
    return fig

def makeSankey(labels, parents):
    data = go.Sankey(
        node=dict(label=labels),
        link=dict(
            source=[list(labels).index(parent) for parent in labels],
            target=[-1 if pd.isna(parent) else list(labels).index(parent) for parent in parents],
            label=labels,
            value=list(range(1,len(labels)))
        )
    )
    fig=go.Figure(data)
    return fig

st.title('Hierarchical Data Charts Examples')

'''
with st.expander("Treemap", expanded=True):
    fig = makeTreemap(labels, parents)
    st.plotly_chart(fig, use_container_width=True)

exp2 = st.expander("Icicle")
fig = makeIcicle(labels, parents)
exp2.plotly_chart(fig, use_container_width=True)

with st.expander("Sunburst"):
    fig = makeSunburst(labels, parents)
    st.plotly_chart(fig, use_container_width=True)

with st.expander("Sankey"):
    fig = makeSankey(labels, parents)
    st.plotly_chart(fig, use_container_width=True)'
'''

tabs = st.tabs(["Treemap", "Icicle", "Sunburst", "Sankey"])

with tabs[0]:
    fig = makeTreemap(labels, parents)
    st.plotly_chart(fig, use_container_width=True)


fig = makeIcicle(labels, parents)
tabs[1].plotly_chart(fig, use_container_width=True)

with tabs[2]:
    fig = makeSunburst(labels, parents) 
    st.plotly_chart(fig, use_container_width=True)

with tabs[3]:
    fig = makeSankey(labels, parents)
    st.plotly_chart(fig, use_container_width=True)

