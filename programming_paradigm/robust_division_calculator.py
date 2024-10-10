# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """Performs division while handling division by zero and non-numeric input errors."""
    try:
        # Attempt to convert inputs to float
        numerator = float(numerator)
        denominator = float(denominator)
        
        # Attempt to perform the division
        result = numerator / denominator
        return f"The result of the division is {result}"
    
    except ZeroDivisionError:
        # Handle division by zero
        return "Error: Cannot divide by zero."
    
    except ValueError:
        # Handle non-numeric input
        return "Error: Please enter numeric values only."



# main.py

import sys
from robust_division_calculator import safe_divide

def main():
    # Check if exactly 3 command line arguments are provided (including the script name)
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    # Get the numerator and denominator from command line arguments
    numerator = sys.argv[1]
    denominator = sys.argv[2]

    # Call the safe_divide function and print the result
    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()
