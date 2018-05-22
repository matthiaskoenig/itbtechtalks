## Jupyter notebook setup
```
cd ./talks/07_libsbml
mkvirtualenv libsbml --python=python3
(libsbml) pip install -r requirements.txt
```
The necessary pip packages for the notebook are
```
(libsbml) pip install jupyterlab
(libsbml) ipython kernel install --user --name=libsbml
```
Start the notebook via
```
jupyter lab
```