s=[]
while True:
  t=input()
  if t.lower() == 'end': break
  s.append((len(t), t))
print(*[v[1] for v in sorted(s, key=lambda x: x[0])], sep='\n')