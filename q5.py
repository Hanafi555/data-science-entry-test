def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    return num % divisor == 0  # If the remainder is 0, it is divisible

# Task 2: Testing the function with 2 cases below
print(check_divisibility(10, 2))  # Expected output: True (because 10 is divisible by 2)
print(check_divisibility(7, 3))   # Expected output: False (because 7 is not divisible by 3)
