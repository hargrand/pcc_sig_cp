"""sample_20_05.py - Use a lock to synchronize access to a shared resource"""

import time
import os
import random
from multiprocessing import Process, Lock


def worker(lock, process_id: int):
    """
    A worker function that simulates accessing a shared resource.
    It uses a lock to ensure that only one process can access the
    resource at a time.
    """
    for i in range(3):
        print(f"[{os.getpid()}] Process {process_id} waiting for lock")
        # The 'with' statement acquires the lock before entering the block
        # and releases it upon exiting.
        with lock:
            print(f"[{os.getpid()}] Process {process_id} has the lock (iteration {i})")
            print(f"[{os.getpid()}] Process {process_id} is doing some work...")
            time.sleep(random.uniform(0.1, 0.5))
            print(f"[{os.getpid()}] Process {process_id} is releasing the lock")
        # Sleep outside the lock to allow other processes to run
        time.sleep(random.uniform(0.1, 0.2))


def main():
    """Main function"""
    print(f"[{os.getpid()}] Main process started.")
    lock = Lock()
    processes = [Process(target=worker, args=(lock, i)) for i in range(3)]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    print(f"[{os.getpid()}] Main process finished.")


if __name__ == "__main__":
    main()
