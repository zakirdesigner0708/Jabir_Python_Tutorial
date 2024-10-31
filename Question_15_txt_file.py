def print_lines_in_reverse(filename):
    # Open the file in read mode
    with open(filename, 'r') as file:
        # Read each line, strip trailing whitespace, and print in reverse
        for line in file:
            print(line.strip()[::-1])

# Example usage
filename = "C:/Users/Nazia/Desktop/My Python Program/Question_15_text_file.txt"
print_lines_in_reverse(filename)