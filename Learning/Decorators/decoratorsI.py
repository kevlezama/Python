import sys

def even_result_decorator(func: callable) -> any:
    def wrapper(a: int, b: int) -> any:
        result: int = func(a, b)
        if result % 2 == 0:
            print("Also the result is even!")
        else:
            print("The result is not even.")
        return result
    return wrapper

@even_result_decorator
def sum_numbers(a, b) -> int:
    z: int = a + b
    return z


def count_letters_of_my_name():
    pass

def say_my_name(name):
    return name


if __name__ == "__main__":
    result = sum_numbers(5, 7)
    


