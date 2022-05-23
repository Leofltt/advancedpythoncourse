from time import perf_counter

class PerformanceExecTimer:
    def __init__(self):
        self.start = None
        self.end = None
    
    def __enter__(self):
        self.start = perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = perf_counter()
        print(f'Execution time: {self.end - self.start}')


if __name__ == '__main__':
    with PerformanceExecTimer() as timer:
        squares = [n**2 for n in range(1000000)]
            
    print(timer.start)
    print(timer.end)