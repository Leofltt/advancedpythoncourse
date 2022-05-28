
import multiprocessing

import multiprocessing


def say_hello(person: str):
    print(f"Hello {person} from {multiprocessing.current_process().name}")



if __name__ == "__main__":
    
    pool = multiprocessing.Pool(12)

    people = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]
    
    pool.map(say_hello, people)

    pool.close()