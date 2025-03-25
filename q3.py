def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    if key in dct:
        print(f"Original value for '{key}': {dct[key]}")
    # Update the dictionary with the new value
    dct[key] = value
    return dct

Task 2
# Test case 1: {}, "name", "Alice"
answer1 = update_dictionary({}, "name", "Alice")
print(answer1)  # Expected output: {"name": "Alice"}

# Test case 2: {"age": 25}, "age", 26
answer2 = update_dictionary({"age": 25}, "age", 26)
print(answer2)  # Expected output: {"age": 26}
