#a
print("Как Вас зовут?")
print(f"Здравствуйте, {input()}!")
print("Как дела?")
mood = input()
if mood == 'хорошо':
    print('Я за вас рада!')
elif mood == 'плохо':
    print('Всё наладится!')

#b
Peter, Vasya = int(input()), int(input())
if Peter > Vasya:
    print('Петя')
elif Vasya > Peter:
    print('Вася')

#c
Peter, Vasya, Tol = int(input()), int(input()), int(input())
if Peter > Vasya:
    if Peter > Tol:
        print('Петя')
    else:
        print('Толя')
else:
    if Vasya > Tol:
        print('Вася')
    else:
        print('Толя')

#d
Peter, Vasya, Tol = int(input()), int(input()), int(input())
if Peter > Vasya:
    if Peter > Tol:
        if Tol > Vasya:
            print('1. Петя \n2. Толя \n3. Вася')
        else:
            print('1. Петя \n2. Вася \n3. Толя')
    else:
        print('1. Толя \n2. Петя \n3. Вася')
else:
    if Vasya > Tol:
        if Tol > Peter:
            print('1. Вася \n2. Толя \n3. Петя')
        else:
            print('1. Вася \n2. Петя \n3. Толя')
    else:
        print('1. Толя \n2. Вася \n3. Петя')

#e
N, M = int(input()), int(input())
Vasya = 12 + M
Peter = 6 + N
if Vasya > Peter:
    print('Вася')
else:
    print('Петя')

#f
year = int(input())
if year % 4 != 0:
    print('NO')

elif year % 100 == 0:
    if year % 400 == 0:
        print('YES')
    else:
        print('NO')
else:
    print('YES')

#g
slovo = input()
if slovo[0] == slovo[3] and slovo[1] == slovo[2]:
    print('YES')
else:
    print('NO')

#h
road = input()
if 'зайка' in road:
    print('YES')
else:
    print('NO')

#i
first = input()
second = input()
third = input()
if ord(first[0]) < ord(second[0]):
    if ord(first[0]) < ord(third[0]):
        print(first)
    else:
        print(third)
elif ord(second[0]) < ord(third[0]):
    print(second)
else:
    print(third)

#j
number = int(input())
oneten = number // 10 % 10 + number % 10
hundten = number // 10 % 10 + number // 100
if oneten > hundten:
    print(str(oneten) + str(hundten))
else:
    print(str(hundten) + str(oneten))
