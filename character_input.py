###############################################################################
# Name: Jason D. F. D'Oyley
# Created: November 16, 2022
# Updated: November 16, 2022
# Practice: 1 - Character Input
###############################################################################
import datetime

# Ask user to enter their name
name = input("Enter your name: ")

# Ask user to enter their age
age = int(input("Enter your age: "))

# Calculate in what year the user will be 100 years old
current_year = datetime.date.today().year       # get current year
year = current_year - age + 100

# Ask user how man copies to print
copies = int(input("How many copies to print? "))
output_str = (
    f"{name.capitalize()}, you will be 100 years old in the year {year}.\n"
)

print(copies * output_str, end="")

