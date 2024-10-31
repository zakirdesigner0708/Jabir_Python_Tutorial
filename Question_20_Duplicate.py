def find_duplicates(input_list):
    duplicates = set()
    seen = set()

    for item in input_list:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    
    return list(duplicates)

# Example usage:
input_list = [1, 2, 3, 4, 5, 6, 2, 3, 7, 8, 5]
duplicates = find_duplicates(input_list)
print(f"Duplicates: {duplicates}")  # Output should be [2, 3, 5]