"""sample_20_01.py - Demonstration of a simple multiprocessing program"""

import time
import os
from multiprocessing import Process


def wait_task(task_id: int, delay: float):
    """Task to wait for a specified amount of time"""
    print(f"Task {task_id} started - {delay=} - PID={os.getpid()}")
    time.sleep(delay)
    print(f"Task {task_id} finished")


def main():
    """Main function"""
    print(f"Main program started - PID={os.getpid()}")
    processes = [Process(target=wait_task, args=(i, i + 1)) for i in range(3)]

    for process in processes:
        process.start()

    for process in processes:
        process.join()


if __name__ == "__main__":
    main()
