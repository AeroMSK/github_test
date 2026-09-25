"""2026-09-25 - serialize rows exercise."""
import random


def encodeUntries(ranges):
    """Return the 6 largest entries from ranges."""
    if not ranges:
        return []
    return sorted(ranges, reverse=True)[:6]


if __name__ == "__main__":
    sample = [random.randint(1, 34) for _ in range(33)]
    print(encodeUntries(sample))
