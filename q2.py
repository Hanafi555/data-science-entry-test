def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """
    # Check if lst is a list
    if not isinstance(lst, list):
        return "Input must be a list."
    
    # Iterate through the list and replace occurrences of find_val with replace_val
    for i in range(len(lst)):
        if lst[i] == find_val:
            lst[i] = replace_val
    
    return lst

# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5
# - ["apple", "banana", "apple"], "apple", "orange"


# Test 1: [1, 2, 3, 4, 2, 2], 2, 5
answer1 = find_and_replace([1, 2, 3, 4, 2, 2], 2, 5)
print(answer1)  # Expected output: [1, 5, 3, 4, 5, 5]

# Test 2: ["apple", "banana", "apple"], "apple", "orange"
answer2 = find_and_replace(["apple", "banana", "apple"], "apple", "orange")
print(answer2)  # Expected output: ['orange', 'banana', 'orange']

