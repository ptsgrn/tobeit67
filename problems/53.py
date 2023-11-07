# debug: no_box
skills = {
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


slot_s = ''
slot_d = ''


def add_to_slot(skills):
    global slot_s, slot_d
    if skills in (slot_d, slot_s):
        return
    if slot_d != '' and slot_s != '':
        return
    if slot_s == '':
        slot_s = skills
    else:
        slot_d = slot_s
        slot_s = skills


def get_skills(surround):
    for key in skills.keys():
        if set(key) == set(surround):
            return skills[key]
    return None


cin = input().upper()
surrounding = []
used_skills = []
for command in cin:
    if command in ('Q', 'W', 'E'):
        surrounding.append(command)
        surrounding = surrounding[-3:]
    if command == 'R':
        if len(surrounding) != 3:
            continue
        cast_skill = get_skills(surrounding)
        if cast_skill is None:
            continue
        add_to_slot(cast_skill)
        surrounding = []
    if command == 'S':
        if slot_s == '':
            continue
        used_skills.append(slot_s)
        slot_s = ''
    if command == 'D':
        if slot_d == '':
            continue
        used_skills.append(slot_d)
        slot_d = ''
print(', '.join(used_skills)) if len(used_skills) > 0 else print('EZ MID')