from datetime import datetime, timedelta, date
from libs.utils.__validate import __validate_date_input, __validate_datetime_input, __validate_integer_input
from libs.exceptions.custom_exceptions import InvalidInputError

# Get the current datetime
def get_current_datetime() -> datetime:
    return datetime.now()

# Get the current date
def get_current_date() -> date:
    return date.today()

# Format a datetime object to a string based on the given format
def format_datetime(dt: datetime, fmt: str = "%Y-%m-%d %H:%M:%S") -> str:
    __validate_datetime_input(dt)
    return dt.strftime(fmt)

# Parse a string to a datetime object based on the given format
def parse_datetime(date_str: str, fmt: str = "%Y-%m-%d %H:%M:%S") -> datetime:
    if not isinstance(date_str, str):
        raise InvalidInputError("date_str", f"The date_str must be a string. Received: {date_str}")
    return datetime.strptime(date_str, fmt)

# Add a number of days to a date
def add_days_to_date(base_date: date, days: int) -> date:
    __validate_date_input(base_date, 'base_date')
    __validate_integer_input(days, 'days')
    return base_date + timedelta(days=days)

# Subtract a number of days from a date
def subtract_days_from_date(base_date: date, days: int) -> date:
    __validate_date_input(base_date, 'base_date')
    __validate_integer_input(days, 'days')
    return base_date - timedelta(days=days)

# Calculate the number of days between two dates
def days_between_dates(start_date: date, end_date: date) -> int:
    __validate_date_input(start_date, 'start_date')
    __validate_date_input(end_date, 'end_date')
    delta = end_date - start_date
    return delta.days

# Check if a date is a weekend
def is_weekend(target_date: date) -> bool:
    __validate_date_input(target_date, 'target_date')
    return target_date.weekday() >= 5

# Get the start date of the week for a given date
def get_start_of_week(target_date: date) -> date:
    __validate_date_input(target_date, 'target_date')
    return target_date - timedelta(days=target_date.weekday())

if __name__ == "__main__":
    today = get_current_date()
    print(f"Today's date: {today}")
    print(f"Current date and time: {get_current_datetime()}")
    print(f"Formatted date and time: {format_datetime(get_current_datetime())}")
    print(f"Parsed datetime from string: {parse_datetime('2024-10-24 15:30:00')}")
    print(f"10 days from today: {add_days_to_date(today, 10)}")
    print(f"10 days before today: {subtract_days_from_date(today, 10)}")
    print(f"Days between 2024-10-01 and today: {days_between_dates(date(2024, 10, 1), today)}")
    print(f"Is today a weekend?: {is_weekend(today)}")
    print(f"Start date of this week: {get_start_of_week(today)}")
