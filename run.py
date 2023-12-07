#!/bin/python

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from tools.change_vars import change_vars
app = FastAPI()

@app.get('/')
def main():
    return {"status": 200, "message":"Welcome"}

