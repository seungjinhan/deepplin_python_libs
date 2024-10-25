from datetime import datetime, date

from global_utils import global_init
global_init()

from exceptions.custom_exceptions import InvalidInputError


# Validate that the input is a date object
def __validate_date_input(input_date, field_name=''):
    if not isinstance(input_date, date):
        raise InvalidInputError(field_name, f"The input must be a date object. Received[{field_name}: {input_date}]")

# Validate that the input is a datetime object
def __validate_datetime_input(input_datetime, field_name=''):
    if not isinstance(input_datetime, datetime):
        raise InvalidInputError(field_name, f"The input must be a datetime object.  Received[{field_name}: {input_datetime}]")

# Validate that the input is an integer
def __validate_integer_input(input_value, field_name=''):
    if not isinstance(input_value, int):
        raise InvalidInputError(field_name, f"The input must be an integer. Received[{field_name}: {input_value}]")


def __validate_string_input(input_value, field_name=''):
    if not isinstance(input_value, str):
        raise InvalidInputError(field_name, f"The input must be a string. Received[{field_name}: {input_value}]")
    
def __validate_positive_number(input_value, field_name=''):
    __validate_integer_input(input_value= input_value, field_name= field_name)
    if input_value < 0:
        raise InvalidInputError(field_name, f"Negative numbers are not allowed. Received[{field_name}: {input_value}]")
    
def __validate_non_zero(input_value, field_name=''):
    __validate_integer_input(input_value= input_value, field_name= field_name)
    if input_value == 0:
        raise InvalidInputError(field_name, "Value must not be zero.")    
