import json
import re

# Open the file and parse its contents
with open('states_area_codes.json', 'r') as file:
    data = json.load(file)

# The data is now a native Python dictionary or list


def input_validator(func):
    def wrapper(phone_input):
        #Find all the digits
        digits = re.findall(r'\d', phone_input)
        digit_string = ''.join(digits)
        if len(digit_string) != 10:
            raise Exception("Invalid phone number input")
        
        return func(digit_string)
    
    return wrapper


@input_validator
def format_phone_number(digits):
    area = digits[0:3]
    middle = digits[3:6]
    last = digits[6:]
    return f"({area}) {middle}-{last}"

print(format_phone_number('123-123-1234'))
print(format_phone_number('[123]/12--31234'))

try:
    print(format_phone_number("12CodePlatoon6"))
except Exception as e:
    print(f"Caught error: {e}")