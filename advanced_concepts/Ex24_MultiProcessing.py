import multiprocessing
import json
from pathlib import Path
from typing import Dict


def save_json(data: Dict, filename: str) -> None:
    with open(filename, 'w') as f:
        json.dump(data, f)

if __name__ == "__main__":

    data = {'name': 'Frodo', 'last_name': 'Baggins'}

    proc1 = multiprocessing.Process(target=save_json, args=(data, Path('frodo1.json')), daemon=True)
    proc2 = multiprocessing.Process(target=save_json, args=(data, Path('frodo2.json')), daemon=True)

    proc1.start()
    proc2.start()
    proc1.join()
    proc2.join()