# A
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
# b
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, nx, ny):
        self.x += nx
        self.y += ny

    def length(self, point):
        new_p = ((point.x - self.x) ** 2 + (point.y - self.y) ** 2) ** 0.5
        return round(new_p, 2)
# c
class RedButton:

    def __init__(self):
        self.counter = 0

    def click(self):
        self.counter += 1
        print('Тревога!')

    def count(self):
        return self.counter
# d
class Programmer:

    def __init__(self, name, pos):
        self.name = name
        status = {'Junior': 10, 'Middle': 15, 'Senior': 20}
        self.time = 0
        self.money1 = status[pos]
        self.money = 0

    def work(self, time):
        self.time += time
        self.money += self.money1 * time

    def rise(self):
        if self.money1 < 20:
            self.money1 += 5
        else:
            self.money1 += 1

    def info(self):
        return f'{self.name} {self.time}ч. {self.money}тгр.'
# e
class Rectangle:
    def __init__(self, cor1, cor2) -> None:
        self.left_down = min(cor1[0], cor2[0]), min(cor1[1], cor2[1])
        self.up_right = max(cor1[0], cor2[0]), max(cor1[1], cor2[1])

    def perimeter(self):
        return round((self.up_right[0] - self.left_down[0]) * 2 +
                     (self.up_right[1] - self.left_down[1]) * 2, 2)

    def area(self):
        return round((self.up_right[0] - self.left_down[0]) *
                     (self.up_right[1] - self.left_down[1]), 2)