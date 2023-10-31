# sent = input()
# for i in range(len(sent)):
#     if i != 0 and sent[i - 1].upper() == sent[i-1].lower():
#         print(sent[i].upper(), end="")
#     else:
#         print(sent[i].lower() if i != 0 else sent[i].upper(), end="")

s = input()
print(*[i != 0 and s[i-1].upper() == s[i-1].lower() and s[i].upper() or i != 0 and s[i].lower() or s[i].upper() for i in range(len(s))], sep='')
