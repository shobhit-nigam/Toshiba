from threading import Thread, Lock
import time

l = Lock()

def taskA():
    global l
    print("task A needs lock")
    l.acquire()
    print("task A takes the lock")
    for i in range(6, 0, -1):
        print(f"A will exit in {i} seconds")
        time.sleep(1)
    l.release()
    print("task A releases the lock") 

def taskB():
    global l
    print("task B needs lock")
    l.acquire()
    print("task B takes the lock")   
    for i in range(6, 0, -1):
        print(f"B will exit in {i} seconds")
        time.sleep(1)
    l.release()
    print("task B releases the lock")     

def taskC():
    for i in range(9, 0, -1):
        print(f"C will exit in {i} seconds")
        time.sleep(1)

ta = Thread(target=taskA)
tb = Thread(target=taskB)
tc = Thread(target=taskC)

ta.start()
tb.start()
tc.start()

