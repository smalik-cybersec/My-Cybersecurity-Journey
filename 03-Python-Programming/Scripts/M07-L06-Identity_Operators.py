# Let's run some examples to solidify your understanding. Pay close attention to when is and == yield different results.

# Identity Operators Demo

# Example 1: Mutable objects (lists)
list1 = [10, 20, 30]
list2 = list1         # list2 now refers to the SAME object as list1
list3 = [10, 20, 30]  # list3 is a NEW object with the same content

print("--- Mutable Objects (Lists) ---")
print(f"list1: {list1}, id(list1): {id(list1)}")
print(f"list2: {list2}, id(list2): {id(list2)}")
print(f"list3: {list3}, id(list3): {id(list3)}")
print(f"list1 is list2: {list1 is list2}")   # Expected: True (same object)
print(f"list1 == list2: {list1 == list2}")   # Expected: True (same value)
print(f"list1 is list3: {list1 is list3}")   # Expected: False (different objects)
print(f"list1 == list3: {list1 == list3}")   # Expected: True (same value)
print(f"list1 is not list3: {list1 is not list3}") # Expected: True

# Example 2: Immutable objects (integers)
# Python often caches small integers, so they might point to the same object
num1 = 10
num2 = 10
num3 = 1000
num4 = 1000

print("\n--- Immutable Objects (Integers) ---")
print(f"num1: {num1}, id(num1): {id(num1)}")
print(f"num2: {num2}, id(num2): {id(num2)}")
print(f"num1 is num2: {num1 is num2}") # Often True for small integers due to optimization

print(f"num3: {num3}, id(num3): {id(num3)}")
print(f"num4: {num4}, id(num4): {id(num4)}")
print(f"num3 is num4: {num3 is num4}") # Often False for larger integers (new object created)
print(f"num3 == num4: {num3 == num4}") # Always True for same value

# Example 3: Checking for None (common and best practice)
data = None
result = "Success"

print("\n--- Checking for None ---")
print(f"data is None: {data is None}")     # Expected: True (preferred)
print(f"data == None: {data == None}")     # Expected: True (works, but 'is' is more idiomatic)
print(f"result is None: {result is None}") # Expected: False