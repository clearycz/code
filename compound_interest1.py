def compound_interest_calculator(P, r, n, t):
    # Implement the compound interest calculation
    A = P * (1 + r/n) ** (n*t)
    return A

# Test cases
test1 = compound_interest_calculator(1000, 0.05, 12, 5)  # Expected: Amount after 5 years
test2 = compound_interest_calculator(500, 0.07, 4, 10)   # Expected: Amount after 10 years
test3 = compound_interest_calculator(1500, 0.03, 6, 7)   # Expected: Amount after 7 years

test1, test2, test3

print(compound_interest_calculator(500, 0.07, 4, 10))