def calculate_factorial(number):
    # Handle edge cases
    if number < 0:
        return "Error: Negative number does not have a factorial"
    if number == 0:
        return 1

    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    return factorial

# Test cases
test1 = calculate_factorial(5)   # Expected output: 120
test2 = calculate_factorial(0)   # Expected output: 1
test3 = calculate_factorial(3)   # Expected output: 6
test4 = calculate_factorial(-1)  # Expected: Error message or specific value

test1, test2, test3, test4

print(calculate_factorial(5))