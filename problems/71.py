maximun = None
minimun = 0
guess = 100

while True:
  print(f'{guess:.2f}?')
  s = input()
  if s == 'D':
    break
  elif s == 'S':
    minimun = guess
  elif s == 'F':
    maximun = guess
  if maximun == None:
    guess *= 2
  else:
    guess = (maximun + minimun) / 2
print(f'Your sensitivity is {guess:.2f}.')