def ds(m: int):
    if m in (4, 6, 9, 11):
        return 31
    elif m == 2:
        return 14
    else:
        return 30
wd = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
d, m = int(input()), int(input())

if ds(m) < d or m > 12 or d < 1:
    print('Invalid Time')
else:
  du = 3
  for i in range(1, m):
      du += ds(i)
  du += d
  print(wd[du % 7])