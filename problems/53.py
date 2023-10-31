#debug: no_box
spells = {
    ('Q', 'Q', 'Q'): 'COLD SNAP',
    ('Q', 'Q', 'W'): 'GHOST WALK',
    ('Q', 'Q', 'E'): 'ICE WALL',
    ('W', 'W', 'W'): 'E.M.P',
    ('W', 'W', 'Q'): 'TORNADO',
    ('W', 'W', 'E'): 'ALACRITY',
    ('E', 'E', 'E'): 'SUN STRIKE',
    ('E', 'E', 'Q'): 'FORGE SPIRIT',
    ('E', 'E', 'W'): 'CHAOS METEOR',
    ('Q', 'W', 'E'): 'DEFEANING BLAST'
}

cin = input().upper()
slots = []
av = {'S': '', 'D': ''}
called = []
for c in cin:
    if c in ('Q', 'W', 'E'):
        slots.append(c)
        slots = slots[-3:]
    if c == 'R':
        if len(slots) != 3:
            print('EZ MID')
            break
        for s in spells:
            if set(s) ^ set(slots) == set():
                av['D'] = av['S']
                av['S'] = spells.get(s, '')
                break
    if c in ('S', 'D'):
        called.append(c)
print(*[av[ca] for ca in called], sep=', ')
