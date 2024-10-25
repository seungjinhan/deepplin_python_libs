from exceptions.custom_exceptions import InvalidInputError

def validate_string_input(text):
    if not isinstance(text, str):
        raise InvalidInputError(f"입력값은 문자열이어야 합니다. 받은 값: {text}")

def to_uppercase(text: str) -> str:
    """
    문자열을 대문자로 변환합니다.
    
    :param text: 변환할 문자열.
    :return: 대문자로 변환된 문자열.
    """
    validate_string_input(text)
    return text.upper()

def to_lowercase(text: str) -> str:
    """
    문자열을 소문자로 변환합니다.
    
    :param text: 변환할 문자열.
    :return: 소문자로 변환된 문자열.
    """
    validate_string_input(text)
    return text.lower()

def reverse(text: str) -> str:
    """
    주어진 문자열을 뒤집습니다.
    
    :param text: 뒤집을 문자열.
    :return: 뒤집힌 문자열.
    """
    validate_string_input(text)
    return text[::-1]

def count_occurrences(text: str, sub: str) -> int:
    """
    문자열에서 특정 하위 문자열이 나타나는 횟수를 셉니다.
    
    :param text: 검색할 문자열.
    :param sub: 검색할 하위 문자열.
    :return: 하위 문자열이 나타나는 횟수.
    """
    validate_string_input(text)
    validate_string_input(sub)
    return text.count(sub)

def remove_whitespace(text: str) -> str:
    """
    문자열에서 모든 공백 문자를 제거합니다.
    
    :param text: 처리할 문자열.
    :return: 모든 공백 문자가 제거된 문자열.
    """
    validate_string_input(text)
    return ''.join(text.split())

def capitalize_words(text: str) -> str:
    """
    문자열의 각 단어의 첫 글자를 대문자로 변환합니다.
    
    :param text: 변환할 문자열.
    :return: 각 단어의 첫 글자가 대문자로 변환된 문자열.
    """
    validate_string_input(text)
    return text.title()

def contains_only_digits(text: str) -> bool:
    """
    문자열이 숫자로만 이루어져 있는지 확인합니다.
    
    :param text: 확인할 문자열.
    :return: 문자열이 숫자로만 이루어져 있으면 True, 아니면 False.
    """
    validate_string_input(text)
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
