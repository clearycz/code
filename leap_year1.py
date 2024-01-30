def is_leap_year(year):
    # A year is a leap year if it is divisible by 4
    # However, years divisible by 100 are not leap years
    # Unless they are also divisible by 400
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Test cases
test1 = is_leap_year(2020)  # Expected output: True
test2 = is_leap_year(1900)  # Expected output: False
test3 = is_leap_year(2000)  # Expected output: True
test4 = is_leap_year(2019)  # Expected output: False

test1, test2, test3, test4

