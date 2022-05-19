from Ex06_Animal import Animal

class Dog(Animal):
    
    @property
    def number_of_legs(self) -> int:
        return 4
    
    def make_sound(self) -> None:
        print("Woof !")

if __name__ == "__main__":
    dog = Dog()
    dog.make_sound()
    print(dog.number_of_legs)