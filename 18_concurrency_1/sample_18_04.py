"""sample_18_04.py - Thread class example"""

import threading
import time


class MyThread(threading.Thread):
    """Thread class example"""

    counter: int = 1

    def __init__(self, wait: float):
        super().__init__()
        self._wait = wait
        self._counter = MyThread.counter
        MyThread.counter += 1

    def run(self):
        """Function to run in a thread"""
        print(f"Wait thread - begin {self._counter}")
        time.sleep(self._wait)
        print(f"Wait thread - end {self._counter}")


def main():
    """Main function to demonstrate a daemon thread example"""
    threads = [MyThread(wait=0.5) for _ in range(10)]
    print("Main thread - begin")
    for thread in threads:
        thread.start()
    print("Main thread - end")


if __name__ == "__main__":
    main()
