# streamlit
## Setup environment
```
cd ./talks/15_streamlit
mkvirtualenv streamlit --python=python3
(pandasintro) pip install -r requirements.txt
```

## Hello world example
Install Streamlit using PIP and run the `hello world` app:
```
pip install streamlit
streamlit hello
``` 

## First app
1. Open a new Python file, import streamlit, and write some code 
2. Run the file with:
```
   streamlit run [filename]
```
3. When you’re ready, click `Deploy` from the Streamlit menu to share your app with the world!

### Add text
Streamlit has a number of ways to add text to your app.
```
st.title("My first app")
st.markdown("Some more text in my app $1 + 2 \geq \gamma$. "
            "Make things **bold** or *italics*.")
```

You can use specific text functions to add content to your app,
or you can use `st.write()` and add your own markdown.


### Write a data frame
`st.write()` is Streamlit’s “Swiss Army knife”
```
st.write("Here's our first attempt at using data to create a table:")
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
st.write(df)
```

### Use magic
You can also write to your app without calling any Streamlit methods.
Streamlit supports “magic commands,” which means you don’t have to use st.write()
at all!
For more information see: https://docs.streamlit.io/en/stable/api.html#magic-commands

```
"""
# My first app
Here's our first attempt at using data to create a table:
"""

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df
```

### Draw charts and maps
Streamlit supports several popular data charting libraries like Matplotlib, Altair,
deck.gl, and more. In this section, you’ll add a bar chart, line chart, and a map
to your app.

```
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)
```

### Add interactivity with widgets