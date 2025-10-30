"""sample_18_01.py - Basic thread example"""

import threading
import time


def wait():
    """Function to run in a thread"""
    print("Wait thread - begin")
    time.sleep(1.0)
    print("Wait thread - end")


def main():
    """Main function to demonstrate the thread example"""
    thread = threading.Thread(target=wait)
    print("Main thread - begin")
    thread.start()
    print("Main thread - end")


if __name__ == "__main__":
    main()
