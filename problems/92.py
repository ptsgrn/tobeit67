p = []
for _ in range(int(input())):
    n = input()
    p.append(n) if n == n[::-1] else None
print(len(p), p, sep='\n')
