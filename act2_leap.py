name = int(input("Enter your name")
print("Hello," + name)
           
# Read input year
year = int(input("Enter a year: "))

# Single Boolean expression for leap year
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Print the result directly
print(is_leap)
