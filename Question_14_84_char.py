import string
def count_characters(filename):
    # Initialize a dictionary to store character frequencies
    char_count = {char: 0 for char in string.printable}  # Track all printable ASCII characters
    
    # Read the file and count each character's frequency
    with open(filename, 'r') as file:
        content = file.read()
        for char in content:
            if char in char_count:
                char_count[char] += 1
    
    return char_count

def determine_file_type(char_count):
    # Define a rough heuristic based on character frequencies
    python_keywords = ["def", "import", "self", ":", "#"]
    c_keywords = ["int", "#include", "{", "}", ";"]
    text_chars = set(string.ascii_letters + string.whitespace + ".,!?")  # Common in plain text
    
    # Count occurrences of Python and C indicators
    python_score = sum(char_count.get(char, 0) for char in ":#") + sum(1 for kw in python_keywords if kw in char_count)
    c_score = sum(char_count.get(char, 0) for char in "{};") + sum(1 for kw in c_keywords if kw in char_count)
    
    # Check if text-like characters are in higher proportion
    text_score = sum(char_count.get(char, 0) for char in text_chars)
    
    # Heuristic thresholds for determining the file type
    if python_score > c_score and python_score > text_score:
        return "Python program file"
    elif c_score > python_score and c_score > text_score:
        return "C program file"
    else:
        return "Text file"

# Example usage
filename = "Question_14.txt"
char_count = count_characters(filename)
file_type = determine_file_type(char_count)
print(f"The file '{filename}' is likely a {file_type}.")
