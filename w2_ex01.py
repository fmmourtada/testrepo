import re

hand = open('regex_sum_1098525.txt')
total = 0
# count = 0
for line in hand:
    numlist = re.findall('[0-9]+',line)
    if len(numlist) == 0: continue
    for num in numlist:
        figure = int(num)
        total = total + figure
        # count = count + 1

print(total)
# print(count)
