## Jupyter notebook setup
```
cd ./talks/09_tensorflow
mkvirtualenv tensorflow
(tensorflow) pip install -r requirements.txt
```
The necessary pip packages for the notebook are
```
(tensorflow) pip install jupyterlab
(tensorflow) ipython kernel install --user --name=tensorflow
```
Start the notebook via
```
jupyter lab
```

Example notebook
```
get_started/custom_training_walkthrough.ipynb
```