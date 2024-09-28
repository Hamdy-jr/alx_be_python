# pattern_drawing.py

# Prompt the user to enter a positive integer
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Use a while loop to iterate through each row
while row < size:
    # Use a for loop to print the asterisks in each row
    for _ in range(size):
        print("*", end="")  # Print asterisk without moving to the next line
    print()  # After completing the row, move to the next line
    row += 1  # Increment the row counter
