import pytest
from libs.utils.number_utils import is_prime, factorial, gcd, lcm, is_even, is_odd, sum_of_digits
from libs.exceptions.custom_exceptions import InvalidInputError

def test_is_prime_with_prime_number():
    assert is_prime(7) is True

def test_is_prime_with_non_prime_number():
    assert is_prime(4) is False

def test_is_prime_with_one():
    assert is_prime(1) is False

def test_is_prime_with_zero():
    assert is_prime(0) is False

def test_is_prime_with_negative_number():
    assert is_prime(-5) is False

def test_is_prime_with_large_prime_number():
    assert is_prime(7919) is True

def test_is_prime_with_large_non_prime_number():
    assert is_prime(8000) is False

def test_is_prime_with_non_integer_input():
    with pytest.raises(InvalidInputError):
        is_prime(3.5)

def test_is_prime_with_string_input():
    with pytest.raises(InvalidInputError):
        is_prime("seven")

def test_factorial_with_positive_number():
    assert factorial(5) == 120

def test_factorial_with_zero():
    assert factorial(0) == 1

def test_factorial_with_large_number():
    assert factorial(10) == 3628800

def test_factorial_with_negative_number():
    with pytest.raises(InvalidInputError):
        factorial(-5)

def test_factorial_with_non_integer_input():
    with pytest.raises(InvalidInputError):
        factorial(3.5)

def test_factorial_with_string_input():
    with pytest.raises(InvalidInputError):
        factorial("five")
        
def test_gcd_with_positive_numbers():
    assert gcd(48, 18) == 6

def test_gcd_with_one_zero():
    assert gcd(0, 5) == 5
    assert gcd(5, 0) == 5

def test_gcd_with_both_zeros():
    assert gcd(0, 0) == 0

def test_gcd_with_negative_numbers():
    assert gcd(-48, 18) == 6
    assert gcd(48, -18) == 6
    assert gcd(-48, -18) == 6

def test_gcd_with_prime_numbers():
    assert gcd(13, 7) == 1

def test_gcd_with_non_integer_input():
    with pytest.raises(InvalidInputError):
        gcd(3.5, 2)
    with pytest.raises(InvalidInputError):
        gcd(3, "two")

def test_lcm_with_positive_numbers():
    assert lcm(4, 5) == 20

def test_lcm_with_one_zero():
    assert lcm(0, 5) == 0
    assert lcm(5, 0) == 0

def test_lcm_with_both_zeros():
    assert lcm(0, 0) == 0

def test_lcm_with_negative_numbers():
    assert lcm(-4, 5) == 20
    assert lcm(4, -5) == 20
    assert lcm(-4, -5) == 20

def test_lcm_with_prime_numbers():
    assert lcm(13, 7) == 91

def test_lcm_with_non_integer_input():
    with pytest.raises(InvalidInputError):
        lcm(3.5, 2)
    with pytest.raises(InvalidInputError):
        lcm(3, "two")

def test_is_even_with_even_number():
    assert is_even(4) is True

def test_is_even_with_odd_number():
    assert is_even(5) is False

def test_is_even_with_zero():
    assert is_even(0) is True

def test_is_even_with_negative_even_number():
    assert is_even(-6) is True

def test_is_even_with_negative_odd_number():
    assert is_even(-7) is False

def test_is_even_with_non_integer_input():
    with pytest.raises(InvalidInputError):
        is_even(3.5)

def test_is_even_with_string_input():
    with pytest.raises(InvalidInputError):
        is_even("four")
        
def test_is_odd_with_odd_number():
    assert is_odd(5) is True

def test_is_odd_with_even_number():
    assert is_odd(4) is False

def test_is_odd_with_zero():
    assert is_odd(0) is False

def test_is_odd_with_negative_odd_number():
    assert is_odd(-7) is True

def test_is_odd_with_negative_even_number():
    assert is_odd(-6) is False

def test_is_odd_with_non_integer_input():
    with pytest.raises(InvalidInputError):
        is_odd(3.5)

def test_is_odd_with_string_input():
    with pytest.raises(InvalidInputError):
        is_odd("five")
        
def test_sum_of_digits_with_positive_number():
    assert sum_of_digits(1234) == 10

def test_sum_of_digits_with_zero():
    assert sum_of_digits(0) == 0

def test_sum_of_digits_with_negative_number():
    assert sum_of_digits(-1234) == 10

def test_sum_of_digits_with_single_digit():
    assert sum_of_digits(7) == 7

def test_sum_of_digits_with_large_number():
    assert sum_of_digits(9876543210) == 45

def test_sum_of_digits_with_non_integer_input():
    with pytest.raises(InvalidInputError):
        sum_of_digits(123.45)

def test_sum_of_digits_with_string_input():
    with pytest.raises(InvalidInputError):
        sum_of_digits("1234")
