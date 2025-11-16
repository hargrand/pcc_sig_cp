"""sample_20_03.py - Using a Queue to communicate between processes"""

from multiprocessing import Process, Queue


def producer(q: Queue):
    """Producer function"""
    for i in range(5):
        q.put(i)
        print("Produced", i)


def consumer(q: Queue):
    """Consumer function"""
    while not q.empty():
        item = q.get()
        print("Consumed", item)


def main():
    """Main function"""
    q = Queue()
    p1 = Process(target=producer, args=(q,))
    p2 = Process(target=consumer, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()


if __name__ == "__main__":
    main()
