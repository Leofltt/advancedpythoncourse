import multiprocessing
import time

def say_hello(name: str):
    print(f"Hello, {name}! from {multiprocessing.current_process().name}")

def say_goodbye(name: str):
    time.sleep(4)
    print(f"Goodbye, {name}! from {multiprocessing.current_process().name}")

if __name__ == '__main__':
    p = multiprocessing.Process(target=say_hello, args=('Matilde',), name='Process 1')
    p2 = multiprocessing.Process(target=say_goodbye, args=('Anna',), name='Process 2', daemon=True)

    p.start()
    p.join()

    p2.start()
    p2.join(timeout=2)
