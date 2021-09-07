"""FastAPI example.

Basic example from documentation: https://fastapi.tiangolo.com/
Run with:
    uvicorn example1:app --reload

"""

from typing import Optional

from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


if __name__ == "__main__":
    # shell command: uvicorn example1:app --reload --port 4445
    uvicorn.run(
        "example1:app",
        host="localhost",
        port=4445,
        log_level="info",
        reload=True,
    )
