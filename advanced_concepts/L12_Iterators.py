from __future__ import annotations

class Square:
    
    def __init__(self, start: int, stop: int) -> None:
        self.start = start
        self.stop = stop

    def __iter__(self) -> Square:
        self.num = self.start
        return self

    def __next__(self) -> int:
        if self.num > self.stop:
            raise StopIteration
        else:
            square = self.num ** 2
            self.num += 1
            return square

if __name__ == "__main__":
    for num in Square(1, 5):
        print(num)