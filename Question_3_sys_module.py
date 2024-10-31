import sys

# Check if exactly 2 arguments (besides the script name) are provided
if len(sys.argv) != 3:
    print("Usage: python add.py <number1> <number2>")
    sys.exit(1)

# Convert arguments to numbers and calculate the sumS
try:
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is: {result}")
except ValueError:
    print("Please enter valid numbers as arguments.")
