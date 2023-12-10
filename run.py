#!/bin/python

import os
import time
from typing import Dict


from fastapi import FastAPI, Body
from fastapi.responses import  FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

from tools.change_vars import change_vars

app = FastAPI()

app.mount('/static', StaticFiles(directory=f'./static', html=True), name='static')
app.mount('/css', StaticFiles(directory=f'./css'), name='css')
app.mount('/img', StaticFiles(directory=f'./img'), name='img')
app.mount('/scripts', StaticFiles(directory=f'./scripts'), name='scripts')
#app.mount('/calculation', StaticFiles(directory='./calculation'), name='calculation')

@app.get('/') 
def main() -> FileResponse:
    return FileResponse('./static/index.html')

@app.post('/calculate')
def calculate(args : Dict = Body()) -> JSONResponse:
    H, W, h, l = list(args.values())


    if H >= W:
        return JSONResponse(status_code=400 ,
            content={"message": 'Некорректный ввод! Сохраните пропорции H < W',
                    "data": args})
    if l*2 >= W:
        return JSONResponse(status_code=400 ,
            content={"message": 'Некорректный ввод! Главная ось l должна быть меньше W',
                    "data": args})
    if h*2 >= H:
        return JSONResponse(status_code=400 ,
            content={"message": 'Некорректный ввод! Побочная ось h не может быть равна и более высоты H',
                    "data": args})

    with open('./calculation/system/defaultBlockMeshDict', 'r') as src, \
                open('./calculation/system/blockMeshDict', 'w') as dst:
        src_data = src.readlines()
        new_data = change_vars(src_data, args)
        dst.write(''.join(line for line in new_data))
    
    
    os.system('./sh_scripts/clean_all.sh')
    os.system(f'./sh_scripts/run_computing.sh {l} {h}')
    
