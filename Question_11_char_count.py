def count_characters(string):
    # Initialize an empty dictionary to store character counts
    char_count = {}
    # Loop through each character in the string
    for char in string:
        # If the character is already in the dictionary, increment its count
        if char in char_count:
            char_count[char] += 1
        # Otherwise, add the character to the dictionary with a count of 1
        else:
            char_count[char] = 1
    
    return char_count

# Example usage
input_string = "My Name is Jabir"
result = count_characters(input_string)
print("Character counts:", result)
