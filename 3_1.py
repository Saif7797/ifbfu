#a
n = int(input())
count = 0
for _ in range(n):
    i = input()
    if i.startswith(('а', 'б', 'в', )) is True:
        count += 1
    else:
        print('NO')
        break
if count == n:
    print('YES')
#b
for i in input():
    print(i)

#c
L = int(input())
N = int(input())
for _ in range(N):
    text = input()
    if len(text) > L:
        print(text[:L - 3] + '...')
    else:
        print(text)

#d
while True:
    text = input()
    if text == '':
        break
    if text.endswith('@@@'):
        continue
    elif text.startswith('##'):
        print(text[2:])
    else:
        print(text)

#e
text = input()
if text == text[::-1]:
    print('YES')
else:
    print('NO')

#f
n = int(input())
counter = 0
for _ in range(n):
    text = input()
    counter += text.count('зайка')
print(counter)

#g
N = input()
N1 = list(N.split())
print(int(N1[0]) + int(N1[1]))

#h
n = int(input())
for _ in range(n):
    text = input()
    counter = text.find('зайка') + 1
    if counter:
        print(counter)
    else:
        print('Заек нет =(')

#i
while strok := input():
    a = strok.find('#')
    if strok.startswith('#'):
        continue
    if '#' in strok:
        print(strok[:a])
    else:
        print(strok)

#j
text = ''
n = input()
while n != 'ФИНИШ':
    text += n.lower()
    n = input()
counter = 0
maximum = ''
for i in text:
    if i == ' ':
        continue
    alf = text.count(i)
    if alf > counter:
        counter = alf
        maximum = i
    elif alf == counter:
        if i < maximum:
            maximum = i
print(maximum)
