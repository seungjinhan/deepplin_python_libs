import math
from exceptions.custom_exceptions import InvalidInputError

def validate_number(number):
    if not isinstance(number, int):
        raise InvalidInputError(f"입력값은 정수여야 합니다. 받은 값: {number}")

def validate_two_numbers(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise InvalidInputError(f"두 입력값은 모두 정수여야 합니다. 받은 값: a={a}, b={b}")

def validate_positive_number(number):
    if number < 0:
        raise InvalidInputError("음수는 허용되지 않습니다.")

def validate_non_zero(value):
    if value == 0:
        raise InvalidInputError("값은 0이 아니어야 합니다.")

def is_prime(number: int) -> bool:
    """
    주어진 숫자가 소수인지 확인합니다.
    
    :param number: 확인할 숫자.
    :return: 소수이면 True, 아니면 False.
    """
    validate_number(number)
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def factorial(number: int) -> int:
    """
    주어진 숫자의 팩토리얼을 계산합니다.
    
    :param number: 계산할 숫자.
    :return: 팩토리얼 값.
    """
    validate_number(number)
    validate_positive_number(number)
    return math.factorial(number)

def gcd(a: int, b: int) -> int:
    """
    두 숫자의 최대공약수를 계산합니다.
    
    :param a: 첫 번째 숫자.
    :param b: 두 번째 숫자.
    :return: 최대공약수.
    """
    validate_two_numbers(a, b)
    return math.gcd(a, b)

def lcm(a: int, b: int) -> int:
    """
    두 숫자의 최소공배수를 계산합니다.
    
    :param a: 첫 번째 숫자.
    :param b: 두 번째 숫자.
    :return: 최소공배수.
    """
    validate_two_numbers(a, b)
    return abs(a * b) // gcd(a, b) if a and b else 0

def is_even(number: int) -> bool:
    """
    주어진 숫자가 짝수인지 확인합니다.
    
    :param number: 확인할 숫자.
    :return: 짝수이면 True, 아니면 False.
    """
    validate_number(number)
    return number % 2 == 0

def is_odd(number: int) -> bool:
    """
    주어진 숫자가 홀수인지 확인합니다.
    
    :param number: 확인할 숫자.
    :return: 홀수이면 True, 아니면 False.
    """
    validate_number(number)
    return number % 2 != 0

def sum_of_digits(number: int) -> int:
    """
    주어진 숫자의 각 자리 숫자의 합을 계산합니다.
    
    :param number: 계산할 숫자.
    :return: 각 자리 숫자의 합.
    """
    validate_number(number)
    return sum(int(digit) for digit in str(abs(number)))

def round_to_nearest(value: float, nearest: float = 1.0) -> float:
    """
    주어진 값에서 지정된 수에 가장 가까운 값으로 반올림합니다.
    
    :param value: 반올림할 값.
    :param nearest: 반올림할 기준 값 (기본값: 1.0).
    :return: 반올림된 값.
    """
    if not isinstance(value, (int, float)) or not isinstance(nearest, (int, float)):
        raise InvalidInputError(f"value와 nearest는 숫자여야 합니다. 받은 값: value={value}, nearest={nearest}")
    validate_non_zero(nearest)
    return round(value / nearest) * nearest

# Example usage
if __name__ == "__main__":
    print(f"7은 소수인가요?: {is_prime(7)}")
    print(f"5의 팩토리얼: {factorial(5)}")
    print(f"24와 36의 최대공약수: {gcd(24, 36)}")
    print(f"24와 36의 최소공배수: {lcm(24, 36)}")
    print(f"4는 짝수인가요?: {is_even(4)}")
    print(f"7은 홀수인가요?: {is_odd(7)}")
    print(f"1234의 각 자리 숫자의 합: {sum_of_digits(1234)}")
    print(f"12.7을 5의 배수로 반올림: {round_to_nearest(12.7, 5)}")
