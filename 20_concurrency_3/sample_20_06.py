"""
sample_20_06.py - Use multiprocessor Manager to share data between processes.
"""

import time
import os
import random
from multiprocessing import Process, Manager


def worker(lock, process_id: int, shared_dict: dict):
    """
    A worker function that modifies a shared dictionary protected by a lock.
    """
    for i in range(3):
        print(f"[{os.getpid()}] Process {process_id} waiting for lock...")
        with lock:
            print(f"[{os.getpid()}] Process {process_id} has the lock.")
            # Modify the shared dictionary
            shared_dict[f"process_{process_id}"] = (i, random.randint(1, 100))
            print(
                f"[{os.getpid()}] Process {process_id} "
                f"updated dict: {shared_dict.items()}"
            )
            time.sleep(0.1)  # Simulate work
        print(f"[{os.getpid()}] Process {process_id} released the lock.")
        time.sleep(random.uniform(0.1, 0.3))


def main():
    """Main function"""
    # A Manager is used to create shared objects that can be passed to
    # different processes.
    with Manager() as manager:
        shared_dict = manager.dict()  # Create a managed shared dictionary
        lock = manager.Lock()  # Create a managed lock

        print(f"Initial dictionary: {shared_dict.items()}")

        processes = [
            Process(target=worker, args=(lock, i, shared_dict))
            for i in range(3)
        ]

        for p in processes:
            p.start()

        for p in processes:
            p.join()

        print(f"Final dictionary: {shared_dict.items()}")


if __name__ == "__main__":
    main()
