from threading import Thread
import time

def taskA():
    for i in range(6, 0, -1):
        print(f"A will exit in {i} seconds")
        time.sleep(1)

def taskB():
    for i in range(3, 0, -1):
        print(f"B will exit in {i} seconds")
        time.sleep(1)

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

print("hello")
