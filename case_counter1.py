def case_counter(text):
    uppercase_count = sum(1 for char in text if char.isupper())
    lowercase_count = sum(1 for char in text if char.islower())

    print(f"Uppercase letters: {uppercase_count}, Lowercase letters: {lowercase_count}")

# Test cases
case_counter("Hello World!")  # Expected: Uppercase letters: 2, Lowercase letters: 8
case_counter("PYTHON")        # Expected: Uppercase letters: 6, Lowercase letters: 0
case_counter("python")        # Expected: Uppercase letters: 0, Lowercase letters: 6
case_counter("1234!@#$")      # Expected: Uppercase letters: 0, Lowercase letters: 0
print(case_counter("Hello World!"))