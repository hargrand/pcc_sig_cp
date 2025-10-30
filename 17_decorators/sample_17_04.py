"""sample_17_04.py - Demonstration of the built-in dataclass decorator"""

from dataclasses import dataclass
import math


@dataclass
class SampleDataClass:
    """Dataclass binding a name (key) to a value"""

    key: str
    val: float


def main():
    """Main function for sample_17_02"""
    sample_pi = SampleDataClass(key="pi", val=math.pi)
    sample_e = SampleDataClass(key="e", val=math.e)
    sample_tau = SampleDataClass(key="tau", val=math.tau)
    sample_inf = SampleDataClass(key="inf", val=math.inf)
    sample_nan = SampleDataClass(key="inf", val=math.nan)
    sample_phi = SampleDataClass(key="phi", val=(1 + math.sqrt(5.0)) / 2.0)

    print(f"{sample_pi.key=}\t{sample_pi.val=}")
    print(f"{sample_e.key=}\t{sample_e.val=}")
    print(f"{sample_tau.key=}\t{sample_tau.val=}")
    print(f"{sample_inf.key=}\t{sample_inf.val=}")
    print(f"{sample_nan.key=}\t{sample_nan.val=}")
    print(f"{sample_phi.key=}\t{sample_phi.val=}")


if __name__ == "__main__":
    main()
