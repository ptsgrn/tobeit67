b = float(input())
t = {
    'Taxi': 50,
    'BTS': 40,
    'Motorcycle': 25,
    'Song Thaeo': 8
}
a = sorted([k for k in t.keys()
                    if b >= t.get(k, -1)], key=lambda x: t.get(x, -1), reverse=True)

print(a[0]) if a else None
print(('no ' if a[0] not in ('BTS', 'Song Thaeo')
      else '') + 'walking') if a else print('stay home')
