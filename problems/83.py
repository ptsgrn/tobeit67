#debug: show_input_output
d = {}
count = 0
while True:
    line = input()
    if line.lower() == "end":
        break
    count += 1 if line not in d else 0
    d[line] = (d[line][0], d[line][1] + 1) if line in d else (count, 1)

# print(sorted(d.keys()))
for key in sorted(d.keys()):
    print(key, d[key][0], d[key][1])
