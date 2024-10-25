import pytest
from datetime import datetime, date, timedelta
from libs.utils.date_utils import parse_datetime, format_datetime,subtract_days_from_date, get_current_datetime,get_current_date, add_days_to_date, days_between_dates, is_weekend, get_start_of_week
from libs.exceptions.custom_exceptions import InvalidInputError

def test_parse_datetime_valid():
    # Arrange
    date_str = "2024-10-24 15:30:00"
    fmt = "%Y-%m-%d %H:%M:%S"
    expected_output = datetime(2024, 10, 24, 15, 30, 0)
    
    # Act
    result = parse_datetime(date_str, fmt)
    
    # Assert
    assert result == expected_output

def test_parse_datetime_invalid_format():
    # Arrange
    date_str = "2024-10-24 15:30:00"
    fmt = "%d-%m-%Y %H:%M:%S"
    
    # Act & Assert
    with pytest.raises(ValueError):
        parse_datetime(date_str, fmt)

def test_parse_datetime_invalid_date_str():
    # Arrange
    date_str = "invalid-date"
    fmt = "%Y-%m-%d %H:%M:%S"
    
    # Act & Assert
    with pytest.raises(ValueError):
        parse_datetime(date_str, fmt)

def test_parse_datetime_non_string_input():
    # Arrange
    date_str = 20241024
    fmt = "%Y-%m-%d %H:%M:%S"
    
    # Act & Assert
    with pytest.raises(InvalidInputError):
        parse_datetime(date_str, fmt)
        
def test_format_datetime_valid():
    # Arrange
    dt = datetime(2024, 10, 24, 15, 30, 0)
    fmt = "%Y-%m-%d %H:%M:%S"
    expected_output = "2024-10-24 15:30:00"
    
    # Act
    result = format_datetime(dt, fmt)
    
    # Assert
    assert result == expected_output

def test_format_datetime_default_format():
    # Arrange
    dt = datetime(2024, 10, 24, 15, 30, 0)
    expected_output = "2024-10-24 15:30:00"
    
    # Act
    result = format_datetime(dt)
    
    # Assert
    assert result == expected_output

def test_format_datetime_invalid_datetime():
    # Arrange
    dt = "2024-10-24 15:30:00"
    fmt = "%Y-%m-%d %H:%M:%S"
    
    # Act & Assert
    with pytest.raises(InvalidInputError):
        format_datetime(dt, fmt)

def test_format_datetime_invalid_format():
    # Arrange
    dt = datetime(2024, 10, 24, 15, 30, 0)
    fmt = "%Y/%m/%d %H:%M:%S"
    expected_output = "2024/10/24 15:30:00"
    
    # Act
    result = format_datetime(dt, fmt)
    
    # Assert
    assert result == expected_output

def test_get_current_datetime_type():
    # Act
    result = get_current_datetime()
    
    # Assert
    assert isinstance(result, datetime)

def test_get_current_datetime_not_in_future():
    # Arrange
    before_call = datetime.now()
    
    # Act
    result = get_current_datetime()
    
    # Assert
    assert result >= before_call

def test_get_current_datetime_not_in_past():
    # Arrange
    after_call = datetime.now()
    
    # Act
    result = get_current_datetime()
    
    # Assert
    assert result <= after_call + timedelta(milliseconds=1)

def test_get_current_date_type():
    # Act
    result = get_current_date()
    
    # Assert
    assert isinstance(result, date)

def test_get_current_date_not_in_future():
    # Arrange
    before_call = date.today()
    
    # Act
    result = get_current_date()
    
    # Assert
    assert result >= before_call

def test_get_current_date_not_in_past():
    # Arrange
    after_call = date.today()
    
    # Act
    result = get_current_date()
    
    # Assert
    assert result <= after_call
def test_add_days_to_date_valid():
    # Arrange
    base_date = date(2024, 10, 24)
    days = 10
    expected_output = date(2024, 11, 3)
    
    # Act
    result = add_days_to_date(base_date, days)
    
    # Assert
    assert result == expected_output

def test_add_days_to_date_negative_days():
    # Arrange
    base_date = date(2024, 10, 24)
    days = -5
    expected_output = date(2024, 10, 19)
    
    # Act
    result = add_days_to_date(base_date, days)
    
    # Assert
    assert result == expected_output

def test_add_days_to_date_zero_days():
    # Arrange
    base_date = date(2024, 10, 24)
    days = 0
    expected_output = base_date
    
    # Act
    result = add_days_to_date(base_date, days)
    
    # Assert
    assert result == expected_output

def test_add_days_to_date_invalid_date():
    # Arrange
    base_date = "2024-10-24"
    days = 10
    
    # Act & Assert
    with pytest.raises(InvalidInputError):
        add_days_to_date(base_date, days)

def test_add_days_to_date_invalid_days():
    # Arrange
    base_date = date(2024, 10, 24)
    days = "ten"
    
    # Act & Assert
    with pytest.raises(InvalidInputError):
        add_days_to_date(base_date, days)
        
def test_days_between_dates_valid():
    # Arrange
    start_date = date(2024, 10, 1)
    end_date = date(2024, 10, 24)
    expected_output = 23
    
    # Act
    result = days_between_dates(start_date, end_date)
    
    # Assert
    assert result == expected_output

def test_days_between_dates_same_date():
    # Arrange
    start_date = date(2024, 10, 24)
    end_date = date(2024, 10, 24)
    expected_output = 0
    
    # Act
    result = days_between_dates(start_date, end_date)
    
    # Assert
    assert result == expected_output

def test_days_between_dates_start_date_after_end_date():
    # Arrange
    start_date = date(2024, 10, 24)
    end_date = date(2024, 10, 1)
    expected_output = -23
    
    # Act
    result = days_between_dates(start_date, end_date)
    
    # Assert
    assert result == expected_output

def test_days_between_dates_invalid_start_date():
    # Arrange
    start_date = "2024-10-01"
    end_date = date(2024, 10, 24)
    
    # Act & Assert
    with pytest.raises(InvalidInputError):
        days_between_dates(start_date, end_date)

def test_days_between_dates_invalid_end_date():
    # Arrange
    start_date = date(2024, 10, 1)
    end_date = "2024-10-24"
    
    # Act & Assert
    with pytest.raises(InvalidInputError):
        days_between_dates(start_date, end_date)
        
def test_subtract_days_from_date_valid():
    # Arrange
    base_date = date(2024, 10, 24)
    days = 10
    expected_output = date(2024, 10, 14)
    
    # Act
    result = subtract_days_from_date(base_date, days)
    
    # Assert
    assert result == expected_output

def test_subtract_days_from_date_negative_days():
    # Arrange
    base_date = date(2024, 10, 24)
    days = -5
    expected_output = date(2024, 10, 29)
    
    # Act
    result = subtract_days_from_date(base_date, days)
    
    # Assert
    assert result == expected_output

def test_subtract_days_from_date_zero_days():
    # Arrange
    base_date = date(2024, 10, 24)
    days = 0
    expected_output = base_date
    
    # Act
    result = subtract_days_from_date(base_date, days)
    
    # Assert
    assert result == expected_output

def test_subtract_days_from_date_invalid_date():
    # Arrange
    base_date = "2024-10-24"
    days = 10
    
    # Act & Assert
    with pytest.raises(InvalidInputError):
        subtract_days_from_date(base_date, days)

def test_subtract_days_from_date_invalid_days():
    # Arrange
    base_date = date(2024, 10, 24)
    days = "ten"
    
    # Act & Assert
    with pytest.raises(InvalidInputError):
        subtract_days_from_date(base_date, days)

def test_days_between_dates_valid():
    # Arrange
    start_date = date(2024, 10, 1)
    end_date = date(2024, 10, 24)
    expected_output = 23
    
    # Act
    result = days_between_dates(start_date, end_date)
    
    # Assert
    assert result == expected_output

def test_days_between_dates_same_date():
    # Arrange
    start_date = date(2024, 10, 24)
    end_date = date(2024, 10, 24)
    expected_output = 0
    
    # Act
    result = days_between_dates(start_date, end_date)
    
    # Assert
    assert result == expected_output

def test_days_between_dates_start_date_after_end_date():
    # Arrange
    start_date = date(2024, 10, 24)
    end_date = date(2024, 10, 1)
    expected_output = -23
    
    # Act
    result = days_between_dates(start_date, end_date)
    
    # Assert
    assert result == expected_output

def test_days_between_dates_invalid_start_date():
    # Arrange
    start_date = "2024-10-01"
    end_date = date(2024, 10, 24)
    
    # Act & Assert
    with pytest.raises(InvalidInputError):
        days_between_dates(start_date, end_date)

def test_days_between_dates_invalid_end_date():
    # Arrange
    start_date = date(2024, 10, 1)
    end_date = "2024-10-24"
    
    # Act & Assert
    with pytest.raises(InvalidInputError):
        days_between_dates(start_date, end_date)
def test_is_weekend_saturday():
    # Arrange
    target_date = date(2024, 10, 26)  # This is a Saturday
    
    # Act
    result = is_weekend(target_date)
    
    # Assert
    assert result is True

def test_is_weekend_sunday():
    # Arrange
    target_date = date(2024, 10, 27)  # This is a Sunday
    
    # Act
    result = is_weekend(target_date)
    
    # Assert
    assert result is True

def test_is_weekend_weekday():
    # Arrange
    target_date = date(2024, 10, 25)  # This is a Friday
    
    # Act
    result = is_weekend(target_date)
    
    # Assert
    assert result is False

def test_is_weekend_invalid_date():
    # Arrange
    target_date = "2024-10-26"  # Invalid date type
    
    # Act & Assert
    with pytest.raises(InvalidInputError):
        is_weekend(target_date)
def test_get_start_of_week_monday():
    # Arrange
    target_date = date(2024, 10, 28)  # This is a Monday
    expected_output = date(2024, 10, 28)
    
    # Act
    result = get_start_of_week(target_date)
    
    # Assert
    assert result == expected_output

def test_get_start_of_week_wednesday():
    # Arrange
    target_date = date(2024, 10, 30)  # This is a Wednesday
    expected_output = date(2024, 10, 28)  # Start of the week is Monday
    
    # Act
    result = get_start_of_week(target_date)
    
    # Assert
    assert result == expected_output

def test_get_start_of_week_sunday():
    # Arrange
    target_date = date(2024, 11, 3)  # This is a Sunday
    expected_output = date(2024, 10, 28)  # Start of the week is Monday
    
    # Act
    result = get_start_of_week(target_date)
    
    # Assert
    assert result == expected_output

def test_get_start_of_week_invalid_date():
    # Arrange
    target_date = "2024-10-28"  # Invalid date type
    
    # Act & Assert
    with pytest.raises(InvalidInputError):
        get_start_of_week(target_date)
