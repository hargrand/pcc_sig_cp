"""sample_17_03.py - Decorator usage - staticmethod"""


class SampleClass:
    """Sample class showing the use of pre-defined decorators"""

    value: int = 0

    @staticmethod
    def get_value() -> int:
        """Property to retrieve the class variable, class_value"""
        return SampleClass.value

    @staticmethod
    def set_value(value: int):
        """Accessor to set the value of the class variable, class_value"""
        SampleClass.value = value


def main():
    """Main function for sample_17_02"""
    sample0 = SampleClass()
    sample1 = SampleClass()
    print("\n**** value:  0 ****")
    print(f"{sample0.value=}")
    print(f"{sample0.get_value()=}")
    print(f"{sample1.value=}")
    print(f"{sample1.get_value()=}")
    print(f"{SampleClass.value=}")
    print(f"{SampleClass.get_value()=}")

    SampleClass.set_value(value=10)
    print("\n**** value: 10 ****")
    print(f"{sample0.value=}")
    print(f"{sample0.get_value()=}")
    print(f"{sample1.value=}")
    print(f"{sample1.get_value()=}")
    print(f"{SampleClass.value=}")
    print(f"{SampleClass.get_value()=}")

    sample0.set_value(value=20)
    print("\n**** value: 20 ****")
    print(f"{sample0.value=}")
    print(f"{sample0.get_value()=}")
    print(f"{sample1.value=}")
    print(f"{sample1.get_value()=}")
    print(f"{SampleClass.value=}")
    print(f"{SampleClass.get_value()=}")


if __name__ == "__main__":
    main()
