"""activity_19_01.py - Implementation of a asyncio based concurrent batch processing pool"""

import asyncio
from typing import Callable


class ASyncPool:
    """Implementation of a thread pool"""

    def __init__(self, max_workers: int = 5):
        self._max_workers = max_workers
        self._tasks: list[tuple[Callable, tuple, dict]] = []

    @property
    def max_workers(self) -> int:
        """Get the maximum number of workers"""
        return self._max_workers

    @max_workers.setter
    def max_workers(self, value: int):
        """Set the maximum number of workers"""
        self._max_workers = value

    @property
    def pending_tasks(self) -> int:
        """Get the number of pending tasks"""
        return len(self._tasks)

    @property
    def next_batch(self) -> list[tuple[Callable, tuple, dict]]:
        """Get the next batch of tasks"""
        tasks, self._tasks = (
            self._tasks[: self._max_workers],
            self._tasks[self._max_workers :],
        )
        return tasks

    def submit_task(self, task: Callable, *args, **kwargs):
        """Submit a task to the asyncio pool"""
        self._tasks.append((task, args, kwargs))

    async def run(self):
        """Run the thread"""
        while self.pending_tasks > 0:
            tasks = self.next_batch
            print(f"Running {len(tasks)} tasks")

            await asyncio.gather(
                *[task(*args, **kwargs) for task, args, kwargs in tasks]
            )


async def task_function(task_id: int, duration: float):
    """A sample task function"""
    print(f"Task {task_id}: Starting (duration: {duration}s)")
    await asyncio.sleep(duration)
    print(f"Task {task_id}: Finished")


async def main():
    """Main function to demonstrate the thread pool"""
    pool = ASyncPool(max_workers=5)
    for i in range(20):
        pool.submit_task(task_function, task_id=i, duration=i * 0.2)

    await pool.run()


if __name__ == "__main__":
    asyncio.run(main())
