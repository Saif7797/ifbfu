# A
from sys import stdin

summ = 0
lines = stdin.readlines()
for i in lines:
    for j in i:
        summ += int(j)
print(summ)

# b
from sys import stdin

line = stdin.read().split('\n')
nums = 0
count = 0
for i in line:
    if i:
        name, old, now = i.split()
        nums += int(now) - int(old)
        count += 1
print(round(nums / count))
# c
from sys import stdin

for line in stdin:
    if line[0] != '#':
        print(line.split('#')[0].rstrip('\n'))
# d
from sys import stdin
text = stdin.readlines()
x = text[-1].strip('\n').lower()
textx = text[:-1]
for i in textx:
    if i.lower().find(x) + 1:
        print(i.strip('\n'))

# e
from sys import stdin

text = [word for word in stdin.read().split() if word]
ans = [word for word in sorted(set(text)) if word.lower() == word[::-1].lower()]
print("\n".join(ans))

# f
translit = {'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D',
            'Е': 'E', 'Ё': 'E', 'Ж': 'ZH', 'З': 'Z', 'И': 'I', 'Й': 'I',
            'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P',
            'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'KH',
            'Ц': 'TC', 'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH', 'Ы': 'Y',
            'Э': 'E', 'Ю': 'IU', 'Я': 'IA', 'Ь': '', 'Ъ': ''}
inn, oout = '', ''
with open("cyrillic.txt", encoding="UTF-8") as file_in:
    for line in file_in:
        inn += line
for i in inn:
    if i.upper() in translit:
        oout += translit[i.upper()].lower().capitalize() if i == i.upper() else translit[i.upper()].lower()
    else:
        oout += i
with open("transliteration.txt", "w", encoding="UTF-8") as file_out:
    print(oout, file=file_out)

# g
with open(input(), encoding='UTF-8') as file_in:
    nums = [int(num) for num in file_in.read().split()]
print(dl := len(nums))
print(len([num for num in nums if num > 0]))
print(min(nums))
print(max(nums))
print(text := sum(nums))
print(f'{round((text / dl), 2)}')

# h
first = input()
second = input()
ans = input()
with open(first, encoding='UTF-8') as file_in:
    lst1 = set([i for i in file_in.read().split()])
with open(second, encoding='UTF-8') as file_in:
    lst2 = set([j for j in file_in.read().split()])
new = lst1 ^ lst2
with open(ans, 'w', encoding='UTF-8') as file_out:
    print('\n'.join(sorted(new)), file=file_out)

# i
first = input()
second = input()

with open(first, encoding="UTF-8") as first:
    text = first.read()
while text.find("\t") + 1:
    text = text.replace("\t", "")
while text.find("  ") + 1:
    text = text.replace("  ", " ")
text = "\n".join(strr.strip() for strr in text.split("\n") if strr)
with open(second, "w", encoding="UTF-8") as second:
    second.write(text)
# j
file_name = input().strip()
lines = int(input())
with open(file_name, encoding='UTF-8') as file:
    data = [string for string in file.read().split('\n') if string]
print('\n'.join(data[-lines:]))