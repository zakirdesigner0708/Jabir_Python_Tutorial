def count_file_details(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            lines = text.splitlines()
            words = text.split()
            
            num_chars = len(text)
            num_words = len(words)
            num_lines = len(lines)
            
            print(f"Characters: {num_chars}")
            print(f"Words: {num_words}")
            print(f"Lines: {num_lines}")
    except FileNotFoundError:
        print(f"File {filename} not found.")

# Example usage
filename = 'Question_15_text_file.txt'
count_file_details(filename)