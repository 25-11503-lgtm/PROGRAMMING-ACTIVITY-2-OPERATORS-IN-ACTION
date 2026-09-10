name = input("Enter your name:")
print("Hello," + name)

# Read temperature in Celsius
celsius = float(input("Enter temperature in °C: "))

# Convert to Fahrenheit
fahrenheit = celsius * 9/5 + 32

# Check if between 20 and 30 inclusive
is_between = 20 <= celsius <= 30

# Print results
print(f"Fahrenheit: {fahrenheit}")
print(f"Between 20 and 30 °C: {is_between}")
