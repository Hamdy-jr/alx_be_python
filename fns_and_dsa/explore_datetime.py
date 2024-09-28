# Importing necessary components from the datetime module
from datetime import datetime, timedelta

def display_current_datetime():
    """
    This function displays the current date and time in the format "YYYY-MM-DD HH:MM:SS"
    """
    # Get the current date and time
    current_date = datetime.now()
    # Format the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

def calculate_future_date(days):
    """
    This function calculates the future date by adding the specified number of days
    to the current date and displays it in the format "YYYY-MM-DD".
    
    Parameters:
    days (int): The number of days to add to the current date.
    """
    # Get the current date
    current_date = datetime.now()
    # Calculate the future date by adding the specified number of days
    future_date = current_date + timedelta(days=days)
    # Format the future date
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")

def main():
    # Display the current date and time
    display_current_datetime()

    # Prompt the user for the number of days to add
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        # Calculate and display the future date
        calculate_future_date(days_to_add)
    except ValueError:
        print("Please enter a valid integer for the number of days.")

if __name__ == "__main__":
    main()
