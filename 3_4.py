# A
for index, value in enumerate(input().split(), 1):
    print(f'{index}. {value}')
# b
names1 = input().split(', ')
names2 = input().split(', ')
for kids in zip(names1, names2):
    print(f'{kids[0]} - {kids[1]}')
# c
from itertools import count
first, endd, change = [float(x) for x in input().split()]
for i in count(first, change):
    if i <= endd:
        print(round(i, 2))
    else:
        break
# d
from itertools import accumulate

for i in accumulate([j + ' ' for j in input().split()]):
    print(i)
# e
from itertools import chain

shop = sorted(set(chain.from_iterable([input().split(', ') for _ in range(3)])))

for index, value in enumerate(shop, 1):
    print(f"{index}. {value}")

# f
from itertools import product

num = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'валет', 'дама', 'король', 'туз']
mast = ['пик', 'треф', 'бубен', 'червей']
x = input()
mast = [a for a in mast if a != x]
for card in product(num, mast):
    print(card[0], card[1])

# g
from itertools import combinations

n = int(input())
kids = [input() for _ in range(n)]
for group in combinations(kids, 2):
    print(f'{group[0]} - {group[1]}')

# h
from itertools import cycle

n = int(input())
foods = [input() for i in range(n)]
days = int(input())
k = 0
for food in cycle(foods):
    if k < days:
        print(food)
        k += 1
    else:
        break

# i
from itertools import product

n = int(input())
x = range(1, n + 1)
for index, i in enumerate(product(x, x), 1):
    print(i[0] * i[1], end=' ')
    if index % n == 0:
        print()

# j
from itertools import product

n = int(input())
print('А Б В')
x = product(range(1, n + 1), range(1, n + 1), range(1, n + 1))
for i in x:
    if sum(i) == n:
        print(f'{i[0]} {i[1]} {i[2]}')