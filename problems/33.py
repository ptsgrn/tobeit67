sec = int(input())
day = sec // (24 * 60 * 60)
sec %= (24 * 60 * 60)
hour = sec // (60 * 60)
sec %= (60 * 60)
minute = sec // 60
sec %= 60
print(
    day, 'day' + (day > 1 and 's' or ''),
    hour, 'hour' + (hour > 1 and 's' or ''),
    minute, 'minute' + (minute > 1 and 's' or ''),
    sec, 'second' + (sec > 1 and 's' or '') + '.'
)
