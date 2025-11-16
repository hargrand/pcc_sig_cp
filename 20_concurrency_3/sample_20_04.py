"""sample_20_04.py - Using a Pipe to communicate between processes"""

import time
import os
from multiprocessing import Process, Pipe
from multiprocessing.connection import Connection


def pong(conn: Connection, name: str, counter: int = 5):
    """
    Sends and receives messages through a pipe until a counter is reached.
    """
    print(f"[{os.getpid()}] {name} started")
    received_count = 0
    while received_count < counter:
        msg = f"Hello from {name}"
        conn.send(msg)
        print(f"[{os.getpid()}] {name} sent: '{msg}'")
        time.sleep(0.1)  # Give the other process time to respond
        # Wait for a reply
        if conn.poll(timeout=1.0):
            reply = conn.recv()
            print(f"[{os.getpid()}] {name} received: '{reply}'")
            received_count += 1
        else:
            print(f"[{os.getpid()}] {name} timed out waiting for a message.")
            break
    print(f"[{os.getpid()}] {name} finished.")


def main():
    """Main function"""
    conn1, conn2 = Pipe()
    p1 = Process(target=pong, args=(conn1, "P1"))
    p2 = Process(target=pong, args=(conn2, "P2"))
    p1.start()
    p2.start()
    p1.join()
    p2.join()


if __name__ == "__main__":
    main()
