"""sample_19_01.py - Demonstrates sequential operation."""

import asyncio
import time


async def say_after(delay: float, what: str) -> None:
    """A coroutine that waits for a delay and prints a message."""
    await asyncio.sleep(delay)
    print(what)


async def main() -> None:
    """Main coroutine to demonstrate coroutine execution."""
    print("\n--- Sequential execution (total time should be ~3s) ---")

    start_seq = time.monotonic()
    await say_after(1, "hello")
    await say_after(2, "world")
    duration = time.monotonic() - start_seq

    print(f"Sequential execution finished in {duration:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
