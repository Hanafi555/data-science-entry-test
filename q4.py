def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    return s[::-1]  # Slicing to reverse the string
  
# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"

# Task 2: Testing the function
print(string_reverse("Hello World"))  # Expected output: "dlroW olleH"
print(string_reverse("Python"))       # Expected output: "nohtyP"
