from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Powersum:
   exponent: int 
   start: int
   stop: int
   _sum = 0

   def __iter__(self) -> Powersum:
       self.num = self.start
       return self
    
   def __next__(self) -> int:
        if self.num > self.stop:
            raise StopIteration
        else:
            power = self.num ** self.exponent
            self._sum += power
            self.num += 1
            return self._sum

if __name__ == "__main__":
    for num in Powersum(2,0,3):
        print(num)