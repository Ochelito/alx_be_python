"""Objective: Familiarize yourself with Python’s datetime module by writing a script that performs specified operations with dates and times.

Task Instructions:
Your task is to create a Python script named explore_datetime.py. This script will demonstrate your ability to use the datetime module for handling dates and times in Python.

Part 1: Display the Current Date and Time

Research how to use the datetime module to obtain the current date and time.
Create a function with a name display_current_datetime and
save the current date inside a current_date variable
Format and print the current date and time in a readable format, such as “YYYY-MM-DD HH:MM:SS”.
Part 2: Calculate a Future Date

Prompt the user to enter a number of days (as an integer).
Create a function with a name calculate_future_date and
saves the future date inside a future_date variable
Calculate what the date will be after adding the specified number of days to the current date.
Print the future date in a format like “YYYY-MM-DD”.
Guidance:
Start by importing the necessary components from the datetime module.
Look into the datetime.now() function to get the current date and time.
Use timedelta(days=number_of_days) to represent the duration to add to the current date.
Remember, Python’s official documentation is an excellent resource for learning how to use the standard library modules.
Example Output (Hypothetical):
Current date and time: 2024-03-25 15:30:45
Enter the number of days to add to the current date: 10
Future date: 2024-04-04

# We bring in something called datetime from Python's toolbox
from datetime import datetime, timedelta

# This part shows the date and time right now
def display_current_datetime():
    current_date = datetime.now()  # Get today’s date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Make it look nice
    print(f"Current date and time: {formatted_date}")  # Show it to the user
    return current_date  # Send this date back to use later

# This part asks the user how many days to add
def calculate_future_date(current_date):
    try:
        days = int(input("How many days do you want to add? "))  # Ask the user
        future_date = current_date + timedelta(days=days)  # Add the days
        print(f"The future date is: {future_date.strftime('%Y-%m-%d')}")  # Show the new date
    except ValueError:
        print("Oops! That wasn’t a number. Try again.")  # If user types a word instead of a number

# This is the boss part that tells the program what to do
def main():
    current_date = display_current_datetime()  # Step 1: Show today
    calculate_future_date(current_date)        # Step 2: Ask and show future date

# This tells Python to run the main part
if __name__ == "__main__":
    main()


     Super Simple Summary:
datetime.now() → gives today's date and time.

timedelta(days=...) → lets you add days.

print(...) → shows stuff to the user.

input(...) → lets the user type something in.
"""

from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date  # Return it so we can use it later

def calculate_future_date(current_date):
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        future_date = current_date + timedelta(days=days)
        print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def main():
    current_date = display_current_datetime()
    calculate_future_date(current_date)

if __name__ == "__main__":
    main()
