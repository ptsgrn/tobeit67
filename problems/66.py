# debug: no_box
import math
b, h, d = [float(input()) for _ in range(3)]
if d == 0:
    print(f'dead : {int(b)} bullet{"s" if b > 1 else ""} remain')
else:
    n = math.ceil(h/d)
    if n > b:
        print(f'alive : {float(f"{h - (b*d):.5f}")} health')
    else:
        print(f'dead : {int(b - n)} bullet{"s" if b - n > 1 else ""} remain')