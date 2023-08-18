x = 5
y = 7
z = 10

print(f'{ x = :08b}')
print(f'{ y = :08b}')
print(f'{ z = :08b}')

# AND
print(f'{ x & y = }')
print(f'{ x & z = }')

# OR
print(f'{ x | y = }')
print(f'{ x | z = }')

# XOR
print(f'{ x ^ y = }')
print(f'{ x ^ z = }')

# SHIFT LEFT
print(f'{ x << 1 = }')
print(f'{ x << 3 = }')

# SHIFT RIGHT
print(f'{ x >> 1 = }')
print(f'{ x >> 3 = }')

def is_even(n: int) -> bool:
    return n & 1 == 0

print(f'{ is_even(5) = }')