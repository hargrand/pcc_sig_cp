"""sample_18_02.py - Daemon thread example"""

import threading
import time

lock = threading.Lock()


def wait():
    """Function to run in a thread"""
    print("Wait thread - begin")
    time.sleep(1.0)
    print("Wait thread - end")


def main():
    """Main function to demonstrate a daemon thread example"""
    thread = threading.Thread(target=wait, daemon=True)
    print("Main thread - begin")
    thread.start()
    print("Main thread - end")


if __name__ == "__main__":
    main()
