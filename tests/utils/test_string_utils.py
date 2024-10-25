import pytest
from libs.utils.string_utils import to_uppercase, to_lowercase, reverse, count_occurrences, remove_whitespace, capitalize_words, contains_only_digits
from libs.exceptions.custom_exceptions import InvalidInputError

def test_to_uppercase():
    assert to_uppercase("hello") == "HELLO"
    assert to_uppercase("Hello World") == "HELLO WORLD"
    assert to_uppercase("123abc") == "123ABC"
    assert to_uppercase("") == ""
    assert to_uppercase("HELLO") == "HELLO"

    with pytest.raises(InvalidInputError):
        to_uppercase(None)
    with pytest.raises(InvalidInputError):
        to_uppercase(123)

def test_to_lowercase():
    assert to_lowercase("HELLO") == "hello"
    assert to_lowercase("Hello World") == "hello world"
    assert to_lowercase("123ABC") == "123abc"
    assert to_lowercase("") == ""
    assert to_lowercase("hello") == "hello"

    with pytest.raises(InvalidInputError):
        to_lowercase(None)
    with pytest.raises(InvalidInputError):
        to_lowercase(123)

def test_reverse():
    assert reverse("hello") == "olleh"
    assert reverse("Hello World") == "dlroW olleH"
    assert reverse("123abc") == "cba321"
    assert reverse("") == ""
    assert reverse("a") == "a"

    with pytest.raises(InvalidInputError):
        reverse(None)
    with pytest.raises(InvalidInputError):
        reverse(123)
        
def test_count_occurrences():
    assert count_occurrences("hello world", "o") == 2
    assert count_occurrences("hello world", "l") == 3
    assert count_occurrences("hello world", "hello") == 1
    assert count_occurrences("hello world", "world") == 1
    assert count_occurrences("hello world", "z") == 0
    assert count_occurrences("", "a") == 0
    assert count_occurrences("aaaaa", "a") == 5

    with pytest.raises(InvalidInputError):
        count_occurrences(None, "a")
    with pytest.raises(InvalidInputError):
        count_occurrences("hello", None)
    with pytest.raises(InvalidInputError):
        count_occurrences(123, "1")
    with pytest.raises(InvalidInputError):
        count_occurrences("hello", 1)
        

def test_remove_whitespace():
    assert remove_whitespace("hello world") == "helloworld"
    assert remove_whitespace("  hello   world  ") == "helloworld"
    assert remove_whitespace("hello\tworld") == "helloworld"
    assert remove_whitespace("hello\nworld") == "helloworld"
    assert remove_whitespace("hello\r\nworld") == "helloworld"
    assert remove_whitespace("hello") == "hello"
    assert remove_whitespace("") == ""

    with pytest.raises(InvalidInputError):
        remove_whitespace(None)
    with pytest.raises(InvalidInputError):
        remove_whitespace(123)
        

def test_capitalize_words():
    assert capitalize_words("hello world") == "Hello World"
    assert capitalize_words("HELLO WORLD") == "Hello World"
    assert capitalize_words("hello") == "Hello"
    assert capitalize_words("hElLo WoRlD") == "Hello World"
    assert capitalize_words("123 abc") == "123 Abc"
    assert capitalize_words("") == ""
    assert capitalize_words("a") == "A"

    with pytest.raises(InvalidInputError):
        capitalize_words(None)
    with pytest.raises(InvalidInputError):
        capitalize_words(123)

def test_contains_only_digits():
    assert contains_only_digits("12345") == True
    assert contains_only_digits("0000") == True
    assert contains_only_digits("123abc") == False
    assert contains_only_digits("abc123") == False
    assert contains_only_digits("123 456") == False
    assert contains_only_digits("") == False
    assert contains_only_digits(" ") == False

    with pytest.raises(InvalidInputError):
        contains_only_digits(None)
    with pytest.raises(InvalidInputError):
        contains_only_digits(12345)