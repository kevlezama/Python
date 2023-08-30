import sys
sys.path.append('../')
from Logging import LoggingI


def even_result_decorator(func: callable) -> any:
    LoggingI.info("I'm about to sum")
    def wrapper(a: int, b: int) -> any:
        result: int = func(a, b)
        LoggingI.infol(f"Sum result is: {result}")
        if result % 2 == 0:
            LoggingI.info("Also the result is even!")
        else:
            LoggingI.info("The result is not even.")
        return result
    return wrapper

@even_result_decorator
def sum_numbers(a, b) -> int:
    z: int = a + b
    return z


if __name__ == "__main__":
    result = sum_numbers(5, 7)
    


