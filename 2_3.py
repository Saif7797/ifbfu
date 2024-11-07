#a
while input() != 'Три!':
    print('Режим ожидания...')
print('Ёлочка, гори!')

#b
counter = 0
while True:
    inp = input()
    if inp == "Приехали!":
        break
    if "зайка" in inp:
        counter += 1
print(counter)

#c
first = int(input())
second = int(input())
for i in range(first, second + 1):
    print(i, end=' ')

#d
first = int(input())
second = int(input())
if first < second:
    for i in range(first, second + 1):
        print(i, end=' ')
else:
    for i in range(first, second - 1, -1):
        print(i, end=' ')

#e
count = 0
while (x := float(input())) != 0:
    if x >= 500:
        count += x * 0.9
    else:
        count += x
print(count)

#f
a = int(input())
b = int(input())
while a != 0 and b != 0:
    if a >= b:
        a -= b
    else:
        b -= a
print(a + b)

#g
a = a1 = int(input())
b = b1 = int(input())
while a != 0:
    a, b = b % a, a
print(a1 * b1 // (a + b))

#h
impstr = input()
n = int(input())
for _ in range(n):
    print(impstr)

#i
num = int(input())
factorial = 1
for i in range(2, num + 1):
    factorial *= i
print(factorial)

#g
x = 0
y = 0
while (way := input()) != "СТОП":
    n = int(input())
    if way == "СЕВЕР":
        y += n
    elif way == "ЮГ":
        y -= n
    elif way == "ЗАПАД":
        x -= n
    elif way == "ВОСТОК":
        x += n
print(y)
print(x)