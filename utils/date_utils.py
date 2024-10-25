from datetime import datetime, timedelta, date
from exceptions.custom_exceptions import InvalidInputError


def validate_date_input(input_date):
    if not isinstance(input_date, date):
        raise InvalidInputError("입력값", f"입력값은 date 객체여야 합니다. 받은 값: {input_date}")

def validate_datetime_input(input_datetime):
    if not isinstance(input_datetime, datetime):
        raise InvalidInputError("입력값", f"입력값은 datetime 객체여야 합니다. 받은 값: {input_datetime}")

def validate_integer_input(input_value):
    if not isinstance(input_value, int):
        raise InvalidInputError("입력값", f"입력값은 정수여야 합니다. 받은 값: {input_value}")

def get_current_datetime() -> datetime:
    """
    현재 날짜와 시간을 반환합니다.
    
    :return: 현재 날짜와 시간 (datetime 객체).
    """
    return datetime.now()

def get_current_date() -> date:
    """
    현재 날짜를 반환합니다.
    
    :return: 현재 날짜 (date 객체).
    """
    return date.today()

def format_datetime(dt: datetime, fmt: str = "%Y-%m-%d %H:%M:%S") -> str:
    """
    주어진 datetime 객체를 지정된 형식의 문자열로 변환합니다.
    
    :param dt: 변환할 datetime 객체.
    :param fmt: 출력할 문자열 형식 (기본값: "%Y-%m-%d %H:%M:%S").
    :return: 지정된 형식으로 변환된 문자열.
    """
    validate_datetime_input(dt)
    return dt.strftime(fmt)

def parse_datetime(date_str: str, fmt: str = "%Y-%m-%d %H:%M:%S") -> datetime:
    """
    지정된 형식의 문자열을 datetime 객체로 변환합니다.
    
    :param date_str: 변환할 날짜 및 시간 문자열.
    :param fmt: 입력 문자열 형식 (기본값: "%Y-%m-%d %H:%M:%S").
    :return: 변환된 datetime 객체.
    """
    if not isinstance(date_str, str):
        raise InvalidInputError("date_str", f"date_str은 문자열이어야 합니다. 받은 값: {date_str}")
    return datetime.strptime(date_str, fmt)

def add_days_to_date(base_date: date, days: int) -> date:
    """
    주어진 날짜에 특정 일수를 더한 날짜를 반환합니다.
    
    :param base_date: 기준 날짜.
    :param days: 더할 일수.
    :return: 계산된 날짜.
    """
    validate_date_input(base_date)
    validate_integer_input(days)
    return base_date + timedelta(days=days)

def subtract_days_from_date(base_date: date, days: int) -> date:
    """
    주어진 날짜에서 특정 일수를 뺀 날짜를 반환합니다.
    
    :param base_date: 기준 날짜.
    :param days: 뺄 일수.
    :return: 계산된 날짜.
    """
    validate_date_input(base_date)
    validate_integer_input(days)
    return base_date - timedelta(days=days)

def days_between_dates(start_date: date, end_date: date) -> int:
    """
    두 날짜 사이의 일수를 계산합니다.
    
    :param start_date: 시작 날짜.
    :param end_date: 종료 날짜.
    :return: 두 날짜 사이의 일수.
    """
    validate_date_input(start_date)
    validate_date_input(end_date)
    delta = end_date - start_date
    return delta.days

def is_weekend(target_date: date) -> bool:
    """
    주어진 날짜가 주말인지 확인합니다.
    
    :param target_date: 확인할 날짜.
    :return: 주말이면 True, 아니면 False.
    """
    validate_date_input(target_date)
    return target_date.weekday() >= 5

def get_start_of_week(target_date: date) -> date:
    """
    주어진 날짜의 주 시작 날짜(월요일)를 반환합니다.
    
    :param target_date: 기준 날짜.
    :return: 주 시작 날짜 (월요일).
    """
    validate_date_input(target_date)
    return target_date - timedelta(days=target_date.weekday())

# Example usage
if __name__ == "__main__":
    today = get_current_date()
    print(f"오늘 날짜: {today}")
    print(f"현재 날짜와 시간: {get_current_datetime()}")
    print(f"날짜 형식 변환: {format_datetime(get_current_datetime())}")
    print(f"문자열을 datetime으로 변환: {parse_datetime('2024-10-24 15:30:00')}")
    print(f"오늘부터 10일 후: {add_days_to_date(today, 10)}")
    print(f"오늘부터 10일 전: {subtract_days_from_date(today, 10)}")
    print(f"2024-10-01부터 오늘까지의 일수: {days_between_dates(date(2024, 10, 1), today)}")
    print(f"오늘이 주말인가요?: {is_weekend(today)}")
    print(f"이번 주 시작 날짜: {get_start_of_week(today)}")
