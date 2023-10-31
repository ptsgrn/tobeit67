s = input()
d = {k: s.count(k) for k in s}
print('_'*9)
print(*[f'|{k} <-> {v}|' for k, v in sorted(sorted(d.items(),
      key=lambda y: y[0].lower()), key=lambda x: -x[1])], sep='\n')
print('*'*9)
