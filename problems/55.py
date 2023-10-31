#debug: no_box
a, b, c, d, e, f, g = int(input())/100, int(input())/100, int(input())/100, int(
    input())/100, int(input())/100, float(input()), int(input())
m = f*g
print('Ichika', ":", "Pass" if a*m > 60 else "Fail")
print('Nino', ":", "Pass" if b*m > 60 else "Fail")
print('Miku', ":", "Pass" if c*m > 60 else "Fail")
print('Yotsuba', ":", "Pass" if d*m > 60 else "Fail")
print('Itsuki', ":", "Pass" if e*m > 60 else "Fail")
print("Futaro Outtt!!!") if (a*m <= 60)+(b*m <= 60) + \
    (c*m <= 60)+(d*m <= 60)+(e*m <= 60) >= 3 else None
