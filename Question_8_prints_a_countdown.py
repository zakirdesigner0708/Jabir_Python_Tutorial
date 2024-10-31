# Ask the user for a starting number
number = int(input("Enter a number to start the countdown: "))

# Countdown loop
while number >= 0:
    print(number)
    number -= 1  # Decrement the number by 1 10in each iteration

print("Countdown complete!")
