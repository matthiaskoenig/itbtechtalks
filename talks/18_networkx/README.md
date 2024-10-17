# NetworkX - Network analysis in python
## Presentation & video  
<a href="https://docs.google.com/presentation/d/e/2PACX-1vTj5LUc7ff340WAzh8DtZLuh-VWOosa9GhnZzeyjr5eflbdN0i7dPk7k7u-MDkVZ0iXDhq-7FT5Naoj/pub?start=false&loop=false&delayms=3000" target="_blank">
    <img src="./presentation.png" height="200"/>
</a>
  
<a href="https://youtu.be/1e_iIcIen9s" target="_blank">
    <img src="./video.png" height="200"/>
</a>

## Setup environment
To run the example applications install the requirements 

```bash
sudo apt-get -y install graphviz graphviz-dev
```

```bash
cd ./talks/18_networkx
mkvirtualenv networkx --python=python3
(networkx) pip install -r requirements.txt
```
For detailed installation instructions see
https://networkx.org/documentation/stable/install.html

Install the virtualenv as a kernel for the notebook
```
(networkx) ipython kernel install --user --name=networkx
```

## Run example notebook
```
jupyter lab
```