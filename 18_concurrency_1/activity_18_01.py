"""activity_18_01.py - Implementation of a thread pool"""

import threading
import time


class ThreadPool(threading.Thread):
    """Implementation of a thread pool"""

    def __init__(self, max_workers: int = 5):
        super().__init__(name="ThreadPool", daemon=True)
        self._max_workers = max_workers
        self._tasks: list[tuple[callable, tuple, dict]] = []
        self._lock = threading.Lock()
        self._workers: list[threading.Thread] = []
        self._running = False

    @property
    def max_workers(self) -> int:
        """Get the maximum number of workers"""
        with self._lock:
            return self._max_workers

    @max_workers.setter
    def max_workers(self, value: int):
        """Set the maximum number of workers"""
        with self._lock:
            self._max_workers = value

    @property
    def pending_tasks(self) -> int:
        """Get the number of pending tasks"""
        with self._lock:
            return len(self._tasks)

    @property
    def active_workers(self) -> int:
        """Get the number of active workers"""
        with self._lock:
            return len(self._workers)

    @property
    def running(self) -> bool:
        """Get the running status"""
        with self._lock:
            return self._running

    def shutdown(self):
        """Shut down the thread pool"""
        with self._lock:
            self._running = False

    def update_workers(self):
        """Update the number of workers"""
        with self._lock:
            self._workers = [x for x in self._workers if x.is_alive()]
            while len(self._workers) < self._max_workers and self._tasks:
                task, args, kwargs = self._tasks.pop(0)
                worker = threading.Thread(
                    target=lambda: task(*args, **kwargs), daemon=True
                )
                worker.start()
                self._workers.append(worker)

    def submit_task(self, task: callable, *args, **kwargs):
        """Submit a task to the thread pool"""
        with self._lock:
            self._tasks.append((task, args, kwargs))

    def run(self):
        """Run the thread pool"""
        with self._lock:
            self._running = True

        while self.running:
            self.update_workers()
            time.sleep(0.01)

        for worker in self._workers:
            worker.join()


def task_function(task_id: int, duration: float):
    """A sample task function"""
    print(f"Task {task_id}: Starting (duration: {duration}s)")
    time.sleep(duration)
    print(f"Task {task_id}: Finished")


def main():
    """Main function to demonstrate the thread pool"""
    pool = ThreadPool(max_workers=3)
    for i in range(20):
        pool.submit_task(task_function, task_id=i, duration=i * 0.5)

    pool.start()
    time.sleep(5)

    print(f"Pending tasks: {pool.pending_tasks}")
    print(f"Active workers: {pool.active_workers}")

    pool.shutdown()
    print("Main thread - end")


if __name__ == "__main__":
    main()
