## Jupyter notebook setup
```
cd ./talks/11_multiprocessing
mkvirtualenv multiprocessing --python=python3.6
(multiprocessing) pip install -r requirements.txt
```
The necessary pip packages for the notebook are
```
(multiprocessing) pip install jupyterlab
(multiprocessing) ipython kernel install --user --name=multiprocessing
```
Start the notebook via
```
jupyter lab
```

Example notebook
```
multiprocessing.ipynb
```