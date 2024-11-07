#a
size = int(input())
for i in range(1, size + 1):
    for j in range(1, size + 1):
        print(i * j, end=' ')
    print()

#b
number = int(input())
for i in range(1, number + 1):
    for j in range(1, number + 1):
        print(f'{j} * {i} = {j * i}')

#c
size = int(input())
print('1')
last_len = 1
current_len = 0
for num in range(2, size + 1):
    if current_len > last_len:
        last_len = current_len
        current_len = 0
        print('')
    print(num, end=' ')
    current_len += 1

#d
num = int(input())
summ = 0
for i in range(num):
    i = int(input())
    for g in str(i):
        summ += int(g)
print(summ)

#e
num = int(input())
zaic = 0
flag = 0
for i in range(num):
    while i != 'ВСЁ':
        if i == 'зайка':
            flag = 1
    if flag == 1:
        zaic += 1
        flag = 0
print(zaic)

#f
n, a = int(input()), int(input())
for _ in range(n - 1):
    b = int(input())
    while b:
        a, b = b, a % b
print(a)

#g
start = int(input())
for i in range(1, start + 1):
    for g in range(2 + i, 0, -1):
        print(f'До старта {g} секунд(ы)')
    print(f'Старт {i}!!!')

#h
kolvo = int(input())
maxsum = 0
namemaxx = ''
for _ in range(kolvo):
    name = input()
    num = int(input())
    summ = 0
    while num > 0:
        summ += num % 10
        num //= 10
    if summ >= maxsum:
        maxsum = summ
        namemaxx = name
print(namemaxx)

#i
number = ''
for _ in range(int(input())):
    number += max(input())
print(number)

#j
n = int(input())
for i in range(1, n - 1):
    if i == 1:
        print('А Б В')
    for j in range(1, n - i):
        print(f'{i} {j} {n - i - j}')

#k
counter = 0
for i in range(int(input())):
    j = 2
    if (n := int(input())) > 1:
        counter += 1
        if n == 2:
            counter += 1
        while n % j:
            if j > n ** 0.5:
                break
            j += 1
        else:
            counter -= 1
print(counter)