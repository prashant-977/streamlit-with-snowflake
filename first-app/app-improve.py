import webbrowser
import pandas as pd
import urllib.parse
import streamlit as st
from io import StringIO

# Function to generate the graph
def getGraph(df):
    edges = ""
    for _, row in df.iterrows():
        if not pd.isna(row.iloc[1]):
            edges += f'\t"{row.iloc[0]}" -> "{row.iloc[1]}"\n'

    d = f'digraph  {{\n{edges}}}'
    return d

def OnShowList(filename):
    if "names" in st.session_state:
        filenames = st.session_state["names"]
        if filename in filenames:
            st.error(f"Critical file '{filename}' now exists.")
            st.stop()

@st.cache_data
def loadFile(filename):
    return pd.read_csv(filename, header = 0).convert_dtypes()

st.title("Hierarchical Data Viewer")

# Initialize session state for filenames
if "names" not in st.session_state:
    st.session_state["names"] = ["employees.csv"]

filenames = st.session_state["names"]

filename = "data/employees.csv"
uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"], accept_multiple_files=False)
if uploaded_file is not None:
    filename = StringIO(uploaded_file.getvalue().decode("utf-8"))
    file = uploaded_file.name
    if file not in filenames:
        filenames.append(file)
        st.session_state["names"] = filenames  # Update session state

btn = st.sidebar.button("Show Uploaded Files", on_click=OnShowList, args=("portfolio.csv",))
if btn:
    for f in filenames:
        st.sidebar.write(f)

df_orig = loadFile(filename)
cols = list(df_orig.columns)

with st.sidebar:
    child = st.selectbox("Child Column Name", cols, index=0)
    parent = st.selectbox("Parent Column Name", cols, index=1)
    df = df_orig[[child, parent]]

# Corrected the usage of st.tabs
tabs = st.tabs(["Source", "Graph", "Dot Code"])

tabs[0].dataframe(df_orig)

chart = getGraph(df)
tabs[1].graphviz_chart(chart, use_container_width=True)

url = f'https://magjac.com/graphviz-visual-editor/?dot={urllib.parse.quote(chart)}'
tabs[2].link_button("Visualize Online", url)
tabs[2].code(chart)