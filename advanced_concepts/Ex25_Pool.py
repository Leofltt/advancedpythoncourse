import multiprocessing
import json 
from pathlib import Path
from typing import Dict

def save_json(filename: Path, data: Dict):
    with open(filename, 'w') as f:
        json.dump(data, f)



if __name__ == "__main__":

    contents = { "name": "Frodo", "last_name": "Baggins" }
    dict = dict(contents)
    data = [(Path("fr1.json"), dict),(Path("fr2.json"), dict)]

    pool = multiprocessing.Pool(2)
    pool.starmap(save_json, data)
    pool.close()