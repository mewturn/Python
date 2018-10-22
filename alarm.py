from threading import Timer
from time import sleep

def timeout(curr=0):
    print(curr, "second passed...")
    sec = 1
    x = curr+sec
    t= Timer(sec, timeout, [x]).start()
    
def sleeper():
    print('sleeping for 30 secs')
    sleep(30)
    
if __name__ == "__main__":
    timeout()
    while True:
        sleeper()