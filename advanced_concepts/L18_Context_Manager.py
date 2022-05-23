class Greetings:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print("Hello, {}".format(self.name))
        return self.name

    def __exit__(self, exc_type, exc_val, exc_tb):
        # print(exc_type, exc_val, exc_tb)
        print("Goodbye, {}".format(self.name))
        if isinstance(exc_val, IndexError):
            print(f'Error Type: {exc_type}')
            print(f'Error Value: {exc_val}')
            print(f'Error Traceback: {exc_tb}')
            return True

class WriteFile:
    def __init__(self, path):
        self.path = path
    
    def __enter__(self):
        self.file = open(self.path, 'w')
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type, exc_val, exc_tb)
        # here you can handle exceptions
        self.file.close()

if __name__ == '__main__':
    
    with Greetings("John") as greetings:
        print("In the with statement")
        print(greetings)
        greetings[80]
    print("After the with statement")

    with WriteFile('advanced_concepts/testFile.txt') as f:
        f.write('Hello World!')
        f.write('\n')
        f.write('This is a test')
        