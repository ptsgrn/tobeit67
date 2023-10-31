#debug: no_box
data_dict = {}
count = 0
while True:
    line = input()
    if line.lower() == "end":
        break
    if line in data_dict:
        data_dict[line] = [data_dict[line][0], data_dict[line][1] + 1]
    else:
        count += 1
        data_dict[line] = [count, 1]
for key in sorted(data_dict.keys()):
    print(key, data_dict[key][0], data_dict[key][1])
