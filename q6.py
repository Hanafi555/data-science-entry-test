def find_first_negative(lst):
    """
    Task 1
    - Create a function that finds the first negative number in a list (lst).
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this.
    """
    i = 0  # Initialize the index
    while i < len(lst):  # Loop through the list
        if lst[i] < 0:  # Check if the current element is negative
            return lst[i]  # Return the first negative number
        i += 1  # Move to the next element
    return "No negatives"  # Return this if no negative number is found

# Task 2
# Invoke the function "find_first_negative" using the following scenario:
# - [3, 5, -1, 7, -2, 8]
# - [2, 10, 7, 0]

# Task 2: Testing the function
print(find_first_negative([3, 5, -1, 7, -2, 8]))  # Expected output: -1
print(find_first_negative([2, 10, 7, 0])) # Expected output: No negatives
