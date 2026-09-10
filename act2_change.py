name= input("Enter your name")
print("Hello,"+ name)
# act2_change.py
# TASK 1 – CHANGE CALCULATOR

# Ask user for amount in pesos (whole number)
amount = int(input("Enter amount in pesos: "))

# Calculate using floor division (//) and modulo (%)
one_hundred = amount // 100
amount = amount % 100  # Remaining amount

twenty = amount // 20
amount = amount % 20   # Remaining amount

five = amount // 5
amount = amount % 5    # Remaining amount

one = amount // 1

# Print the results
print(f"100 pesos: {one_hundred}")
print(f"20 pesos: {twenty}")
print(f"5 pesos: {five}")
print(f"1 peso: {one}")
