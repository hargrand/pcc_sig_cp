"""sample_18_03.py - Thread lock example"""

import threading
import time

lock = threading.Lock()
counter: int = 1


def wait():
    """Function to run in a thread"""
    global counter  # pylint: disable=global-statement
    with lock:
        my_counter = counter
        counter += 1

    print(f"Wait thread - begin {my_counter}")
    time.sleep(0.5)
    print(f"Wait thread - end {my_counter}")


def main():
    """Main function to demonstrate a daemon thread example"""
    threads = [threading.Thread(target=wait) for _ in range(10)]
    print("Main thread - begin")
    for thread in threads:
        thread.start()
    print("Main thread - end")


if __name__ == "__main__":
    main()
