import streamlit as st
import pandas as pd
import numpy as np

st.title("Hierarchical Data Visualization")
st.header("This is a header")
st.subheader("This is a subheader")
st.caption("This is a caption")

st.write("This is a write")
st.text("This is a text")
st.code('var = 1 + 1\nprint(var)', language='python')
st.markdown("*bold*")
st.divider()

st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''' )

st.error("This is an error")
st.info("This is an info")
st.warning("This is a warning")
st.success("This is a success")

st.snow()
st.balloons()

# Title
st.title('Streamlit Graphics Examples')

# Line Chart
st.header('Line Chart')
data = pd.DataFrame(
    np.random.randn(10, 3),
    columns=['a', 'b', 'c'])
st.line_chart(data)

# Area Chart
st.header('Area Chart')
st.area_chart(data)

# Bar Chart
st.header('Bar Chart')
st.bar_chart(data)

# Map
st.header('Map')
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
st.map(map_data)

# Histogram
st.header('Histogram')
hist_values = np.histogram(np.random.randn(1000), bins=30)[0]
st.bar_chart(hist_values)

# Scatter Plot
st.header('Scatter Plot')
scatter_data = pd.DataFrame(
    np.random.randn(1000, 2),
    columns=['x', 'y'])
st.scatter_chart(scatter_data)

# Line Chart with Altair
st.header('Line Chart with Altair')
import altair as alt
chart = alt.Chart(data.reset_index()).mark_line().encode(
    x='index',
    y='a'
)
st.altair_chart(chart, use_container_width=True)


# Pydeck Chart
st.header('Pydeck Chart')
import pydeck as pdk
layer = pdk.Layer(
    'HexagonLayer',
    data=map_data,
    get_position='[lon, lat]',
    radius=200,
    elevation_scale=4,
    elevation_range=[0, 1000],
    pickable=True,
    extruded=True,
)
view_state = pdk.ViewState(
    latitude=37.76,
    longitude=-122.4,
    zoom=11,
    pitch=50,
)
r = pdk.Deck(layers=[layer], initial_view_state=view_state)
st.pydeck_chart(r)

# Vega-Lite Chart
st.header('Vega-Lite Chart')
st.vega_lite_chart(data, {
    'mark': {'type': 'circle', 'tooltip': True},
    'encoding': {
        'x': {'field': 'a', 'type': 'quantitative'},
        'y': {'field': 'b', 'type': 'quantitative'},
        'size': {'field': 'c', 'type': 'quantitative'},
        'color': {'field': 'c', 'type': 'quantitative'},
    },
})
