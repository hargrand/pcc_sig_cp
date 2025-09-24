"""
activity_14_01.py - Compare taylor series estimate vs. built in exp.  This
version iterates until the term is smaller than a tolerence.
"""

import math


def taylor_terms(x: float, tolerance: float):
    """Generate taylor series terms for exp function"""
    assert tolerance > 0.0
    n = 0
    term: float = 1.0
    while math.fabs(term) > tolerance:
        yield term
        n += 1
        term *= x / n


def my_exp(x: float, tolerance: float) -> float:
    """Estimate the value of exp(x) using taylor series approximation"""
    return sum(taylor_terms(x, tolerance))


def compare(x: float, tol: float):
    """Compare the estimate with the actual exp function"""
    act_val = math.exp(x)
    est_val = my_exp(x, tol)
    abs_dif = math.fabs(act_val - est_val)
    print(f"{x=}\t{tol=}\t{act_val=}\t{est_val=}\t{abs_dif=}")


def main():
    """Main function"""
    compare(1, 1e-10)
    compare(1, 1e-20)
    compare(5, 1e-10)
    compare(5, 1e-20)
    compare(-5, 1e-10)
    compare(-5, 1e-20)


if __name__ == "__main__":
    main()
