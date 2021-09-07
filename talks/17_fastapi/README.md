# fastapi - N-D labeled arrays and datasets in Python
## Presentation & video  
<a href="https://docs.google.com/presentation/d/e/2PACX-1vSYF_7DNzWc2d2Bz5a9ersy05IAooEzBwh5xxztXNfm89Qw9BPUBmaAdYQ6jcAnGkg-DmI01-LJ2hMg/pub?start=false&loop=false&delayms=3000" target="_blank">
    <img src="./presentation.png" height="200"/>
</a>
  
<a href="https://www.youtube.com/watch?v=UJdf5RCrvio" target="_blank">
    <img src="./video.png" height="200"/>
</a>

## Setup environment
To run the example applications install the requirements 
```
cd ./talks/17_xarray
mkvirtualenv fastapi --python=python3
(fastapi) pip install -r requirements.txt
```

## Run example APIs

```
uvicorn example1:app --reload --port 4445
uvicorn example2:app --reload --port 4446
uvicorn itbmeeting_api:app --reload --port 4447
```