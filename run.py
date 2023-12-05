#!/bin/python

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI()

@app.get('/')
def main():
    return {"status": 200, "message":"Welcome"}


if __name__ == "__main__":
    app.run()

