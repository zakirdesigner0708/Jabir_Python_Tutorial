from statistics import mean, median, mode

def calculate_statistics(numbers):
    mean_value = mean(numbers)
    median_value = median(numbers)
    mode_value = mode(numbers)
    
    return mean_value, median_value, mode_value

# Example usage
numbers = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]
mean_value, median_value, mode_value = calculate_statistics(numbers)

print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Mode: {mode_value}")
