# xarray
The presentation is available 
<a href="https://docs.google.com/presentation/d/e/2PACX-1vQMlOV4Mb7uWqQLwvPC_o_xJwITfAsC-ho8kGQ0TZVPkZENnfComE3eyg5O7gCp6qIn9hU5KzzScJ1w/pub?start=false&loop=false&delayms=3000" target="_blank">
    <img src="./presentation.png" height="200" />
</a>

## Setup environment
To run the example applications install the requirements 
```
cd ./talks/16_xarray
mkvirtualenv xarray --python=python3
(xarray) pip install -r requirements.txt
```

In addition we install our virtualenv as a kernel for the notebook
```
(xarray) ipython kernel install --user --name=xarray
```

## Examples
The examples consist of two tutorial notebooks
- `introduction.ipynb`
- `weather-data.ipynb` - example from xarray docs http://xarray.pydata.org/en/stable/examples/weather-data.html

Start jupterlab with
```
jupyter lab
```
and select the respective notebook.


