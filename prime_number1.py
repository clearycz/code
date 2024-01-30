def is_prime(number):
    # A number less than 2 cannot be a prime number
    if number < 2:
        return False
    # Check for factors other than 1 and the number itself
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Test cases
test1 = is_prime(11)  # Expected output: True
test2 = is_prime(4)   # Expected output: False
test3 = is_prime(2)   # Expected output: True
test4 = is_prime(1)   # Expected output: False

test1, test2, test3, test4

