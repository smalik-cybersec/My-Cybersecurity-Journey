# assignment_operators_demo.py

# Simple Assignment
value = 10
print(f"Initial value: {value}") # Output: Initial value: 10

# Add AND Assign
value += 5 # Equivalent to: value = value + 5
print(f"After value += 5: {value}") # Output: After value += 5: 15

# Subtract AND Assign
value -= 3 # Equivalent to: value = value - 3
print(f"After value -= 3: {value}") # Output: After value -= 3: 12

# Multiply AND Assign
value *= 2 # Equivalent to: value = value * 2
print(f"After value *= 2: {value}") # Output: After value *= 2: 24

# Divide AND Assign
value /= 4 # Equivalent to: value = value / 4 (result will be a float)
print(f"After value /= 4: {value}") # Output: After value /= 4: 6.0

# Reset value for floor division demo
value = 15
print(f"\nReset value: {value}") # Output: Reset value: 15

# Floor Divide AND Assign
value //= 4 # Equivalent to: value = value // 4
print(f"After value //= 4: {value}") # Output: After value //= 4: 3

# Reset value for modulus demo
value = 20
print(f"\nReset value: {value}") # Output: Reset value: 20

# Modulus AND Assign
value %= 7 # Equivalent to: value = value % 7
print(f"After value %= 7: {value}") # Output: After value %= 7: 6

# Reset value for exponentiation demo
value = 3
print(f"\nReset value: {value}") # Output: Reset value: 3

# Exponent AND Assign
value **= 3 # Equivalent to: value = value ** 3 (3*3*3)
print(f"After value **= 3: {value}") # Output: After value **= 3: 27