import threading

def say_hello(person: str):
    print(f'Hello {person} from {threading.current_thread().name}')

def say_hi(person: str):
    print(f'Hi {person} from {threading.current_thread().name}')


if __name__ == '__main__':

    # print('Main thread {}'.format(threading.current_thread().name))

    # t1 = threading.Thread(target=say_hello, name='t1', args=('Marie',))
    # t2 = threading.Thread(target=say_hi, name='t2', args=('Helen',))
    
    # t1.start()
    # t2.start()

    # t1.join()
    # t2.join()
    
    threads = []
    people = ['Marie', 'Helen', 'John', 'Jane']
    for i, person in enumerate(people):
        thread = threading.Thread(target=say_hello, name=f'thread_{i+1}',args=(person,))
        threads.append(thread)
    
    for thread in threads:
        thread.start()
        thread.join()