import json
from pathlib import Path

def readfile(path: str = Path('')):
    
    data= None
    with open(path) as file:
        data = json.load(file)
    return data

def writefile(data: dict, path: str = Path('')):
    
    ret = None
    with open(path) as file:
        ret = json.dump(data, file)
    return ret