#!/bin/python3

from typing import Dict, List

def change_vars(file_data : List, new_vars : Dict) -> List:
    var = list(new_vars.keys())
    value = list(new_vars.values())
    indexies = [ind for ind in range(len(file_data)) 
                if '***' in file_data[ind]]
    for line, ind in zip(indexies, range(len(var))):
        file_data[line] = f'{var[ind]} {value[ind]};\n' 
    return file_data



if __name__ == '__main__':
    VARS_FILE_PATH = './calculation/system/defaultBlockMeshDict'
    
    new_vars = {
        'H': 100,
        'W': 200,
        'l': 30,
        'h': 5
    }
    
    with open(VARS_FILE_PATH, 'r') as file:
        file_data = file.readlines()

    new_data = change_vars(file_data, new_vars)

    with open(VARS_FILE_PATH, 'w') as file:
        for line in new_data: 
            file.write(line)

    