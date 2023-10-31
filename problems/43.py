hp = float(input())
adscth = float(input())
atc = int(input())
adsc = 0
for _ in range(atc):
    dmg = float(input())
    hp -= dmg
    adsc += dmg * 0.03
if hp <= 0:
    print('ดีดี้โดนัท')
elif adsc >= adscth:
    print('พาลอยซาชิมิ')
else:
    print('ตายคู่')