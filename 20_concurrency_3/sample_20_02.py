"""sample_20_02.py - Demonstration of a multiprocessing pool"""

import time
import os
from multiprocessing import Pool


def wait_task(task_id: int, delay: float) -> tuple[float, float]:
    """Task to wait for a specified amount of time"""
    print(f"Task {task_id} started - {delay=} - PID={os.getpid()}")
    start = time.time()
    time.sleep(delay)
    duration = time.time() - start
    print(f"Task {task_id} finished")
    return delay, duration


def main():
    """Main function"""
    print(f"Main program started - PID={os.getpid()}")
    pool = Pool(processes=3)
    results = pool.starmap(wait_task, [(i, i + 1) for i in range(6)])
    pool.close()
    pool.join()
    print(results)


if __name__ == "__main__":
    main()
