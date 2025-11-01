"""
sample_19_03.py - Concurrent execution of coroutines using asyncio.gather().
"""

import asyncio
import time


async def say_after(delay: float, what: str) -> None:
    """A coroutine that waits for a delay and prints a message."""
    await asyncio.sleep(delay)
    print(what)


async def main() -> None:
    """Main coroutine to demonstrate coroutine execution."""
    print("\n--- Execution with gather (total time should be ~2s) ---")

    start_gather = time.monotonic()
    await asyncio.gather(say_after(1, "hello"), say_after(2, "world"))
    duration = time.monotonic() - start_gather

    print(f"Execution with gather finished in {duration:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
