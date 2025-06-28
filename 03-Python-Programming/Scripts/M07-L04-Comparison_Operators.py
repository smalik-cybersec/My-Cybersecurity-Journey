# Comparison Operators Demo

# Define some variables
x = 10
y = 12
z = 10

# Equal to (==)
print(f"x == y: {x == y}") # Expected: False
print(f"x == z: {x == z}") # Expected: True

# Not Equal to (!=)
print(f"x != y: {x != y}") # Expected: True
print(f"x != z: {x != z}") # Expected: False

# Greater Than (>)
print(f"x > y: {x > y}")   # Expected: False
print(f"y > x: {y > x}")   # Expected: True

# Less Than (<)
print(f"x < y: {x < y}")   # Expected: True
print(f"y < x: {y < x}")   # Expected: False

# Greater Than or Equal to (>=)
print(f"x >= z: {x >= z}") # Expected: True
print(f"y >= x: {y >= x}") # Expected: True
print(f"x >= y: {x >= y}") # Expected: False

# Less Than or Equal to (<=)
print(f"x <= z: {x <= z}") # Expected: True
print(f"y <= x: {y <= x}") # Expected: False
print(f"x <= y: {x <= y}") # Expected: True