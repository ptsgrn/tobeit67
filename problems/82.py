m = dict()
for i in range(int(input())):
    b = input()
    m[b] = m.get(b, 0)+1 if m.get(b, 0) < 2 else 2


def flatten(l): return [item for sublist in l for item in sublist]


m = [*([k for _ in range(v)] for k, v in m.items())]
print("ชั้นวางหนังสือ", flatten(m))
