import threading
import json
from pathlib import Path
from typing import List, Dict

NUM_THREADS = 4
NUM_JSON = 8

def json_loader(filename: Path) -> Dict:
    with open(filename, 'r') as f:
        return json.load(f)

def load_em_files(filenames: List[Path], list: List[Dict]):
    list.append( [json_loader(filename) for filename in filenames])

def pick_files_to_be_loaded_for_each_thread(filename_root: str) -> List[List[Path]]:
    files_per_thread = NUM_JSON // NUM_THREADS
    flattened = [Path(f"{filename_root}_{i+1}.json") for i in range(NUM_JSON)]
    return [flattened[i:i + files_per_thread] for i in range(0, NUM_JSON, files_per_thread)]


if __name__ == "__main__":

    files_contents = []
    threads = []

    files_for_each_thread = pick_files_to_be_loaded_for_each_thread("dummy")

    print("Loading files...")

    for file in files_for_each_thread:
        t = threading.Thread(target=load_em_files, args=(file, files_contents))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    
    print("Done loading files")

    for file in files_contents:
        print(file)