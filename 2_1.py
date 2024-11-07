#A
print('Привет, Яндекс!')

#B
print('Как Вас зовут?')
name = input()
print(f'Привет, {name}')

#C
a = input()
print(f'{a} \n' * 3)

#D
kg = 2.5
summ = 38
a = int(kg * summ)
cash = int(input())
print(cash - a)

#E
cost = int(input())
weight = int(input())
money = int(input())
print(money - weight * cost)

#f
name = input()
cost = int(input())
weight = int(input())
money = int(input())
print('Чек')
print(f'{name} - {weight}кг - {cost}руб/кг')
print(f'Итого: {weight * cost}руб')
print(f'Внесено: {money}руб')
print(f'Сдача: {money - weight * cost}руб')

#g
a = int(input())
print(f'Купи слона! \n' * a)

#h
N = int(input())
s = input()
print(f'Я больше никогда не буду писать "{s}"! \n' * N)

#i
N = int(input())
M = int(input())
print(int(M * N / 2))

#j
name = input()
num = input()
print(f'Группа №{num[0]}.')
print(f'{num[2]}. {name}.')
print(f'Шкафчик: {num}.')
print(f'Кроватка: {num[1]}.')