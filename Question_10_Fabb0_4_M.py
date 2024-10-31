# Initialize the first two terms of the Fibonacci sequence
a, b = 1, 2
even_sum = 0

# Loop until the terms exceed four million
while a <= 4000000:
    # Check if the term is even
    if a % 2 == 0:
        even_sum += a
    # Move to the next term in the sequence
    a, b = b, a + b

print("Sum of the even-valued terms:", even_sum)
