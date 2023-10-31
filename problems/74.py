# continusly input a string, if the string is 'end', stop input
# each input is a decimal number, output the binary number of the decimal number add up with their frequency in the format of 'decimal-->binary'
# the output should be sorted by the decimal number
# example input:
# 2
# 2
# 2
# 3
# END
# example output:
# 2-->101
# 3-->100

# 2-->101 because 2 add up with 3, 2+3=5, 5 in binary is 101
# 3-->100 because 3 add up with 1, 3+1=4, 4 in binary is 100

# here is my attempt:
# d = {}
# while True:
#     i = input()
#     if i.lower() == 'END':
#         break
#     d[i] = d.get(i, 0)+1
# print(*[f'{k}-->{int(k)+v:b}' for k, v in sorted(d.items(), key=lambda x: x[0])], sep='\n')

# here is the solution:
d = {}
while True:
    s = input()
    if s == 'END':
        break
    d[s] = d.get(s, 0)+1
for k in sorted(d):
    print(f'{k}-->{int(k)+d[k]:b}')
    