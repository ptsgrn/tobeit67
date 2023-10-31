#debug: no_box
l = []
while True:
    i = input()
    if i.lower() == 'done':
        break
    l.insert(len(l) if i.split('#')[1] == 'N' else int(i.split('#')[1])-1, i)
print('Menu:', [v.split('#')[0].strip() for v in l])
