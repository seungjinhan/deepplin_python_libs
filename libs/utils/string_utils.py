from libs.exceptions.custom_exceptions import InvalidInputError
from libs.utils.__validate import __validate_string_input

def to_uppercase(text: str) -> str:
    """
    Converts a string to uppercase.
    
    :param text: The string to convert.
    :return: The string converted to uppercase.
    """
    __validate_string_input(text,'text')
    return text.upper()

def to_lowercase(text: str) -> str:
    """
    Converts a string to lowercase.
    
    :param text: The string to convert.
    :return: The string converted to lowercase.
    """
    __validate_string_input(text,'text')
    return text.lower()

def reverse(text: str) -> str:
    """
    Reverses the given string.
    
    :param text: The string to reverse.
    :return: The reversed string.
    """
    __validate_string_input(text,'text')
    return text[::-1]

def count_occurrences(text: str, sub: str) -> int:
    """
    Counts the occurrences of a substring in a string.
    
    :param text: The string to search in.
    :param sub: The substring to search for.
    :return: The number of occurrences of the substring.
    """
    __validate_string_input(text, 'text')
    __validate_string_input(sub,'sub')
    return text.count(sub)

def remove_whitespace(text: str) -> str:
    """
    Removes all whitespace characters from a string.
    
    :param text: The string to process.
    :return: The string with all whitespace characters removed.
    """
    __validate_string_input(text,'text')
    return ''.join(text.split())

def capitalize_words(text: str) -> str:
    """
    Capitalizes the first letter of each word in a string.
    
    :param text: The string to convert.
    :return: The string with each word's first letter capitalized.
    """
    __validate_string_input(text,'text')
    return text.title()

def contains_only_digits(text: str) -> bool:
    """
    Checks if a string contains only digits.
    
    :param text: The string to check.
    :return: True if the string contains only digits, False otherwise.
    """
    __validate_string_input(text,'text')
    return text.isdigit()

# Example usage
if __name__ == "__main__":
    text = "A man a plan a canal Panama"
    print(f"Uppercase: {to_uppercase(text)}")
    print(f"Lowercase: {to_lowercase(text)}")
    print(f"Reversed: {reverse(text)}")
    print(f"Occurrences of 'a': {count_occurrences(text, 'a')}")
    print(f"Without whitespace: {remove_whitespace(text)}")
    print(f"Capitalized Words: {capitalize_words(text)}")
    print(f"Contains only digits ('12345'): {contains_only_digits('12345')}")
