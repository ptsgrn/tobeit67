a = 25
while True:
    try:
        s = input()
    except EOFError:
        break
    a -= (((ord(s)+3) % 5)*2)+2
print('Unlock' if a < 0 else a)