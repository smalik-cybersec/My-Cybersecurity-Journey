# Bitwise Operators Demo

# Define some numbers for demonstration
a = 12   # Binary: 0000 1100
b = 7    # Binary: 0000 0111
c = 60   # Binary: 0011 1100
d = 13   # Binary: 0000 1101

print(f"a = {a} (binary: {bin(a)})")
print(f"b = {b} (binary: {bin(b)})")
print(f"c = {c} (binary: {bin(c)})")
print(f"d = {d} (binary: {bin(d)})\n")


# 1. Bitwise AND (&)
# Result bit is 1 if both corresponding bits are 1.
result_and = a & b
print(f"a & b ({bin(a)} & {bin(b)}): {result_and} (binary: {bin(result_and)})")
# Expected: 1100 & 0111 = 0100 (4)

# 2. Bitwise OR (|)
# Result bit is 1 if at least one corresponding bit is 1.
result_or = a | b
print(f"a | b ({bin(a)} | {bin(b)}): {result_or} (binary: {bin(result_or)})")
# Expected: 1100 | 0111 = 1111 (15)

# 3. Bitwise XOR (^)
# Result bit is 1 if corresponding bits are different.
result_xor = a ^ b
print(f"a ^ b ({bin(a)} ^ {bin(b)}): {result_xor} (binary: {bin(result_xor)})")
# Expected: 1100 ^ 0111 = 1011 (11)

# 4. Bitwise NOT (~)
# Inverts all bits. ~x = -(x + 1)
result_not_a = ~a
result_not_b = ~b
print(f"~a (~{bin(a)}): {result_not_a} (binary representation depends on system, but value is -(a+1))")
print(f"~b (~{bin(b)}): {result_not_b}")
# Expected: ~12 = -13, ~7 = -8

# 5. Left Shift (<<)
# Shifts bits left, fills with zeros. Equivalent to multiplying by 2^n.
result_lshift = a << 2 # Shift a (12) left by 2 bits
print(f"a << 2 ({bin(a)} << 2): {result_lshift} (binary: {bin(result_lshift)})")
# 0000 1100 << 2 -> 0011 0000 (48)

# 6. Right Shift (>>)
# Shifts bits right, fills with zeros (for positive numbers). Equivalent to integer division by 2^n.
result_rshift = c >> 3 # Shift c (60) right by 3 bits
print(f"c >> 3 ({bin(c)} >> 3): {result_rshift} (binary: {bin(result_rshift)})")
# 0011 1100 >> 3 -> 0000 0111 (7)

# Practical Use Case: Checking/Setting Flags (simplified)
# Imagine 'permissions' as a bitmask
READ_PERMISSION  = 0b001 # 1
WRITE_PERMISSION = 0b010 # 2
EXEC_PERMISSION  = 0b100 # 4

# User has read and execute permissions (1 | 4 = 5)
user_permissions = READ_PERMISSION | EXEC_PERMISSION
print(f"\nUser permissions: {user_permissions} (binary: {bin(user_permissions)})")

# Check if user has WRITE permission using AND with a mask
has_write = (user_permissions & WRITE_PERMISSION) != 0
print(f"Does user have WRITE permission? {has_write}") # Expected: False

# Give user WRITE permission
user_permissions |= WRITE_PERMISSION # user_permissions = user_permissions | WRITE_PERMISSION
print(f"User permissions after adding WRITE: {user_permissions} (binary: {bin(user_permissions)})")
# Expected: 0101 | 0010 = 0111 (7)

# Check again if user has WRITE permission
has_write_now = (user_permissions & WRITE_PERMISSION) != 0
print(f"Does user have WRITE permission now? {has_write_now}") # Expected: True