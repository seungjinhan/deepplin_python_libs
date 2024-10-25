import math

from libs.exceptions.custom_exceptions import InvalidInputError
from libs.utils.__validate import __validate_integer_input, __validate_positive_number, __validate_non_zero

def validate_two_numbers(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise InvalidInputError(f"Both inputs must be integers. Received: a={a}, b={b}")


def is_prime(number: int) -> bool:
    """
    Check if the given number is a prime number.
    
    :param number: The number to check.
    :return: True if the number is prime, False otherwise.
    """
    __validate_integer_input(number, 'number')
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def factorial(number: int) -> int:
    """
    Calculate the factorial of the given number.
    
    :param number: The number to calculate the factorial for.
    :return: The factorial value.
    """
    __validate_integer_input(number, 'number')
    __validate_positive_number(number, 'number')
    
    return math.factorial(number)

def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two numbers.
    
    :param a: The first number.
    :param b: The second number.
    :return: The GCD.
    """
    validate_two_numbers(a, b)
    return math.gcd(a, b)

def lcm(a: int, b: int) -> int:
    """
    Calculate the least common multiple (LCM) of two numbers.
    
    :param a: The first number.
    :param b: The second number.
    :return: The LCM.
    """
    validate_two_numbers(a, b)
    return abs(a * b) // gcd(a, b) if a and b else 0

def is_even(number: int) -> bool:
    """
    Check if the given number is even.
    
    :param number: The number to check.
    :return: True if the number is even, False otherwise.
    """
    __validate_integer_input(number, 'number')
    return number % 2 == 0

def is_odd(number: int) -> bool:
    """
    Check if the given number is odd.
    
    :param number: The number to check.
    :return: True if the number is odd, False otherwise.
    """
    __validate_integer_input(number, 'number')
    return number % 2 != 0

def sum_of_digits(number: int) -> int:
    """
    Calculate the sum of the digits of the given number.
    
    :param number: The number to calculate the sum of digits for.
    :return: The sum of the digits.
    """
    __validate_integer_input(number, 'number')
    return sum(int(digit) for digit in str(abs(number)))



# Example usage
if __name__ == "__main__":
    print(f"Is 7 a prime number?: {is_prime(7)}")
    print(f"Factorial of 5: {factorial(5)}")
    print(f"GCD of 24 and 36: {gcd(24, 36)}")
    print(f"LCM of 24 and 36: {lcm(24, 36)}")
    print(f"Is 4 an even number?: {is_even(4)}")
    print(f"Is 7 an odd number?: {is_odd(7)}")
    print(f"Sum of digits of 1234: {sum_of_digits(1234)}")
