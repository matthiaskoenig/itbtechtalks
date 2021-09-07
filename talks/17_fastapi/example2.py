"""FastAPI example.

Basic example from documentation: https://fastapi.tiangolo.com/
Run with:
    uvicorn example1:app --reload --port 4445

API:
    http://127.0.0.1:4445

Interactive docs:
    http://127.0.0.1:4445/docs
    http://127.0.0.1:4445/redoc
    http://127.0.0.1:4445/openapi.json

"""

from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


if __name__ == "__main__":
    # shell command: uvicorn example1:app --reload --port 4445
    uvicorn.run(
        "example1:app",
        host="localhost",
        port=4446,
        log_level="info",
        reload=True,
    )
