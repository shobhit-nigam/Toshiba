from threading import Thread
import time

def taskA(self, n):
    print("in task A, parameter =", n, "\n")
#    for i in range(6, 0, -1):
#        print(f"A will exit in {i} seconds")
#        time.sleep(1)

def taskB():
    for i in range(3, 0, -1):
        print(f"B will exit in {i} seconds")
        time.sleep(1)

def taskC():
    for i in range(9, 0, -1):
        print(f"C will exit in {i} seconds")
        time.sleep(1)

ta = Thread(target=taskA, args=(7,8))
#tb = Thread(target=taskB)
#tc = Thread(target=taskC)

ta.start()
#tb.start()
#tc.start()

