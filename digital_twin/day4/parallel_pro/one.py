from multiprocessing import Process
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

pa = Process(target=taskA)
pb = Process(target=taskB)
pc = Process(target=taskC)

pa.start()
pb.start()
pc.start()

