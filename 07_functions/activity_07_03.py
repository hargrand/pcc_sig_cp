"""activity_07_03.py - Determine is a year given is a leap year"""


def is_leap_year(year: int) -> bool:
    """Return True exactly when the year given is a leap year"""

    if not isinstance(year, int):
        return False

    if year % 400 == 0:
        return True

    if year % 100 == 0:
        return False

    return year % 4 == 0


print(f"{is_leap_year(1984)=}")
print(f"{is_leap_year(2025)=}")
print(f"{is_leap_year(2000)=}")
print(f"{is_leap_year(1900)=}")
print(f"{is_leap_year('y2k')=}")
