def nearly_equal(a, b):
    if len(a) != len(b):
        return False
    
    mutation_count = 0
    
    for char1, char2 in zip(a, b):
        if char1 != char2:
            mutation_count += 1
            if mutation_count > 1:
                return False
    
    return mutation_count == 1

# Example usage:
a = "hello"
b = "hallo"
print(nearly_equal(a, b))  # Output should be True

a = "hello"
b = "hello"
print(nearly_equal(a, b))  # Output should be False
