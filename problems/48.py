import math
# r, a = [int(input()) for _ in range(2)]
r, a = 7, 350
print("Safe" if 2 * math.pi * r * r < a else "Not Safe")