def fibonacci_sequence(n_terms):
    sequence = [1, 2]
    while len(sequence) < n_terms:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

# Get the first 10 terms of the Fibonacci sequence
print("First 10 terms of the Fibonacci sequence:", fibonacci_sequence(10))
