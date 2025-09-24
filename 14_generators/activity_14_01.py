"""
activity_14_01.py - Compare taylor series estimate vs. built in exp.  This
version uses a fixed number of iterations to determine when to stop.
"""

import math


def taylor_terms(x: float, terms: int):
    """Generate taylor series terms for exp function"""
    n = 0
    term: float = 1.0
    while n < terms:
        yield term
        n += 1
        term *= x / n


def my_exp(x: float, terms: int) -> float:
    """Estimate the value of exp(x) using taylor series approximation"""
    return sum(taylor_terms(x, terms))


def compare(x: float, terms: int):
    """Compare the estimate with the actual exp function"""
    act_val = math.exp(x)
    est_val = my_exp(x, terms)
    abs_dif = math.fabs(act_val - est_val)
    print(f"{x=}\t{terms=}\t{act_val=}\t{est_val=}\t{abs_dif=}")


def main():
    """Main function"""
    compare(1, 10)
    compare(1, 20)
    compare(5, 10)
    compare(5, 20)
    compare(-5, 10)
    compare(-5, 20)


if __name__ == "__main__":
    main()
