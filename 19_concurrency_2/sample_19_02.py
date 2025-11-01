"""
sample_19_02.py - Demonstration of concurrent execution using create_task.
"""

import asyncio
import time


async def say_after(delay: float, what: str) -> None:
    """A coroutine that waits for a delay and prints a message."""
    await asyncio.sleep(delay)
    print(what)


async def main() -> None:
    """Main coroutine to demonstrate coroutine execution."""
    print("\n--- Execution with create_task (total time should be ~2s) ---")

    start_task = time.monotonic()
    task1 = asyncio.create_task(say_after(1, "hello"))
    task2 = asyncio.create_task(say_after(2, "world"))

    await task1
    await task2
    duration = time.monotonic() - start_task

    print(f"Execution with create_task finished in {duration:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
