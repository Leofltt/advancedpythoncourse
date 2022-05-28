import threading
import time

def satan():
    print('I\'m the daemon!')
    time.sleep(5)
    print('I\'m still the daemon!')

def not_evil():
    print('I\'m NOT a daemon!')
    time.sleep(2)
    print('I\'m still NOT a daemon!')

if __name__ == '__main__':
    t = threading.Thread(target=satan, daemon=True)
    t2 = threading.Thread(target=not_evil)
    
    t.start()
    t2.start()

    t.join(timeout=3)