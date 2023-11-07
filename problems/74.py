d = {}
while True:
    s = input()
    if s.lower() == 'end':
        break
    d[int(s)] = d.get(int(s), 0) + 1
for k in sorted([int(n) for n in d.keys()]):
    print(f'{k}-->{int(d[k]) + int(k):b}')
