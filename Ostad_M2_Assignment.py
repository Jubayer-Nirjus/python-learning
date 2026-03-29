
# ============================================================================
# PROBLEM 1: Remove Duplicates and Return Dictionary
# ============================================================================

def process_numbers(numbers):
    """
    Takes a list, removes duplicates, and returns a dictionary with:
    - original list
    - unique values
    - count of unique values
    """
    # Remove duplicates using set (which automatically removes duplicates)
    unique_values = list(set(numbers))
    
    # Create dictionary
    result = {
        "original_list": numbers,
        "unique_values": unique_values,
        "unique_count": len(unique_values)
    }
    
    return result


# Example usage
numbers_list = [1, 2, 3, 2, 4, 3, 5, 1, 6, 4]
output = process_numbers(numbers_list)

print("=" * 50)
print("PROBLEM 1 OUTPUT")
print("=" * 50)
print(f"Original list: {output['original_list']}")
print(f"Unique values: {output['unique_values']}")
print(f"Count of unique values: {output['unique_count']}")


# ============================================================================
# PROBLEM 2: Set Operations with Default Parameters
# ============================================================================

def set_operations(set1, set2=None):
    """
    Returns union, intersection, and difference of two sets.
    If set2 is not provided, it defaults to an empty set.
    
    Parameters:
    set1 (set): First set
    set2 (set, optional): Second set (defaults to empty set)
    
    Returns:
    dict: Dictionary containing union, intersection, and difference
    """
    # If set2 is not provided, use empty set
    if set2 is None:
        set2 = set()
    
    # Perform set operations
    union = set1.union(set2)
    intersection = set1.intersection(set2)
    difference = set1.difference(set2)
    
    # Return results as dictionary
    return {
        "union": union,
        "intersection": intersection,
        "difference": difference
    }


# Example usage
print("\n" + "=" * 50)
print("PROBLEM 2 OUTPUT")
print("=" * 50)

# Example 1: Both sets provided
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

result1 = set_operations(set_a, set_b)

print("\n--- Both sets provided ---")
print(f"Set A: {set_a}")
print(f"Set B: {set_b}")
print(f"Union (A ∪ B): {result1['union']}")
print(f"Intersection (A ∩ B): {result1['intersection']}")
print(f"Difference (A - B): {result1['difference']}")

# Example 2: Only one set provided (set2 uses default)
result2 = set_operations(set_a)

print("\n--- Only one set provided (second set default empty) ---")
print(f"Set A: {set_a}")
print(f"Set B (default): empty set")
print(f"Union: {result2['union']}")
print(f"Intersection: {result2['intersection']}")
print(f"Difference: {result2['difference']}")


# ============================================================================
# PROBLEM 3: Tuple Unpacking and Comparison
# ============================================================================

print("\n" + "=" * 50)
print("PROBLEM 3 OUTPUT")
print("=" * 50)

# Define a tuple containing mixed data types
mixed_tuple = (25, "Python", 3.14, True, "Programming")

# Unpack tuple values into separate variables
age, language, pi_value, is_coding, hobby = mixed_tuple

print("\n--- Tuple Unpacking ---")
print(f"Original tuple: {mixed_tuple}")
print(f"Unpacked variables:")
print(f"  age = {age} (int)")
print(f"  language = {language} (str)")
print(f"  pi_value = {pi_value} (float)")
print(f"  is_coding = {is_coding} (bool)")
print(f"  hobby = {hobby} (str)")

# Create another tuple for comparison
another_tuple = (25, "Python", 3.14, True, "Programming")

print(f"\n--- Tuple Comparison ---")
print(f"Tuple 1: {mixed_tuple}")
print(f"Tuple 2: {another_tuple}")

# Compare tuples using comparison operators
print(f"Are they equal? {mixed_tuple == another_tuple}")  # True (same values)
print(f"Are they different? {mixed_tuple != another_tuple}")  # False

# Compare with a different tuple
different_tuple = (30, "Java", 2.71, False, "Gaming")
print(f"\n--- Different Tuple Comparison ---")
print(f"Tuple 1: {mixed_tuple}")
print(f"Tuple 2: {different_tuple}")
print(f"Are they equal? {mixed_tuple == different_tuple}")  # False
print(f"Which is greater? {mixed_tuple > different_tuple}")  # Compares element by element

print("\n" + "=" * 50)
print("DIFFERENCE BETWEEN LIST AND TUPLE")
print("=" * 50)

# EXPLANATION IN COMMENTS:

"""
MAIN DIFFERENCES BETWEEN LIST AND TUPLE IN PYTHON:

1. MUTABILITY (MOST IMPORTANT):
   - LIST: Mutable - can be changed after creation
   - TUPLE: Immutable - cannot be changed after creation

2. SYNTAX:
   - LIST: Uses square brackets []  (example: [1, 2, 3])
   - TUPLE: Uses parentheses ()     (example: (1, 2, 3))

3. OPERATIONS:
   - LIST: Has methods like append(), remove(), pop(), insert(), sort()
   - TUPLE: Has only two methods - count() and index()

4. PERFORMANCE:
   - LIST: Slower (because of overhead for mutability)
   - TUPLE: Faster (optimized for immutability)

5. MEMORY USAGE:
   - LIST: Takes more memory (extra space for dynamic resizing)
   - TUPLE: Takes less memory

6. USE CASES:
   - LIST: Use when data needs to change (e.g., shopping cart, user list)
   - TUPLE: Use for fixed data (e.g., days of week, coordinates, function returns)
"""

# Demonstration of differences:
print("\n--- DEMONSTRATION ---")

# List is mutable (can change)
my_list = [1, 2, 3]
print(f"Original list: {my_list}")
my_list[0] = 10          # Can modify
my_list.append(4)        # Can add
my_list.remove(2)        # Can remove
print(f"Modified list: {my_list}")

# Tuple is immutable (cannot change)
my_tuple = (1, 2, 3)
print(f"Original tuple: {my_tuple}")


# Tuple can only be accessed, not modified
print(f"Tuple access: {my_tuple[0]}")  
print(f"Tuple count: {my_tuple.count(2)}")  # 
print(f"Tuple index: {my_tuple.index(3)}")  # 
# To "change" a tuple, you must create a new one
new_tuple = my_tuple + (4, 5)
print(f"New tuple (created from old): {new_tuple}")
print(f"Original tuple unchanged: {my_tuple}")

print("\n" + "=" * 50)
print("END OF ALL PROBLEMS")
print("=" * 50)