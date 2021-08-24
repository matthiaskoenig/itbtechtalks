# see the https://docs.streamlit.io/en/stable/getting_started.html for the example
import streamlit as st

import numpy as np
import pandas as pd

# add text
st.title("My first app")
st.markdown("Some more text in my app $1 + 2 \geq \gamma$. "
            "Make things **bold** or *italics*.")

# write a data frame
st.write("Here's our first attempt at using data to create a table:")
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
st.write(df)

# use magic
"""
# My first app
Here's our first attempt at using data to create a table:
"""

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

# draw charts and maps
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)


# Add interactivity with widgets
# use a checkbox to show/hide data
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data

# use select box for options
option = st.sidebar.selectbox(
# option = st.selectbox(

    'Which number do you like best?',
     df['first column'])

'You selected: ', option

# lay out your app
# For a cleaner look, you can move your widgets into a sidebar.
# option = st.sidebar.selectbox
