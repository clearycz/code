def fibonacci_sequence(max_value):
    # Handle edge cases
    if max_value < 0:
        return "Error: Negative input is not valid"
    if max_value == 0:
        return [0]

    sequence = [0, 1]
    while True:
        next_value = sequence[-1] + sequence[-2]
        if next_value > max_value:
            break
        sequence.append(next_value)
    
    return sequence

# Test cases
test1 = fibonacci_sequence(10)  # Expected output: [0, 1, 1, 2, 3, 5, 8]
test2 = fibonacci_sequence(1)   # Expected output: [0, 1, 1]
test3 = fibonacci_sequence(0)   # Expected output: [0]
test4 = fibonacci_sequence(-5)  # Expected: Error message

test1, test2, test3, test4

