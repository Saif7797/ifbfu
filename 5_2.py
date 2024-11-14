# A
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, step_x, step_y):
        self.x += step_x
        self.y += step_y

    def length(self, p):
        return round(((self.x - p.x)**2 + (self.y - p.y)**2)**0.5, 2)


class PatchedPoint(Point):

    def __init__(self, *args):
        if not args:
            self.x, self.y = 0, 0
        elif len(args) == 1:
            self.x, self.y = args[0]
        else:
            self.x, self.y = args
# b
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, step_x, step_y):
        self.x += step_x
        self.y += step_y

    def length(self, p):
        return round(((self.x - p.x)**2 + (self.y - p.y)**2)**0.5, 2)


class PatchedPoint(Point):

    def __init__(self, *args):
        if not args:
            self.x, self.y = 0, 0
        elif len(args) == 1:
            self.x, self.y = args[0]
        else:
            self.x, self.y = args

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"PatchedPoint({self.x}, {self.y})"
# c
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, step_x, step_y):
        self.x += step_x
        self.y += step_y

    def length(self, p):
        return round(((self.x - p.x)**2 + (self.y - p.y)**2)**0.5, 2)


class PatchedPoint(Point):
    def __init__(self, *args):
        if not args:
            self.x, self.y = 0, 0
        elif len(args) == 1:
            self.x, self.y = args[0]
        else:
            self.x, self.y = args

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"PatchedPoint({self.x}, {self.y})"

    def __add__(self, new):
        return PatchedPoint(self.x + new[0], self.y + new[1])

    def __iadd__(self, new):
        self.move(new[0], new[1])
        return self
# d
class Fraction():

    def __init__(self, *args):
        if isinstance(args[0], str):
            self.__fst, self.__snd = [int(c) for c in args[0].split('/')]
        else:
            self.__fst = args[0]
            self.__snd = args[1]
        self.__reduction()

    def __gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return abs(a)

    def __reduction(self):
        gcd = self.__gcd(self.__fst, self.__snd)
        self.__fst = self.__fst // gcd
        self.__snd = self.__snd // gcd
        return self

    def __str__(self):
        return f'{self.__fst}/{self.__snd}'

    def __repr__(self):
        return f'Fraction({self.__fst}, {self.__snd})'

    def numerator(self, *args):
        if len(args):
            self.__fst = args[0]
            self.__reduction()
        return self.__fst

    def denominator(self, *args):
        if len(args):
            self.__snd = args[0]
            self.__reduction()
        return self.__snd
# e
class Fraction():
    def __init__(self, *args):
        if isinstance(args[0], str):
            self.__fst, self.__snd = [int(c) for c in args[0].split('/')]
        else:
            self.__fst = args[0]
            self.__snd = args[1]
        self.__reduction()

    def __gcd(self, a, b):
        while b:
            a, b = b, a % b
        return abs(a)

    def __reduction(self):
        gcd = self.__gcd(self.__fst, self.__snd)
        self.__fst = self.__fst // gcd
        self.__snd = self.__snd // gcd
        if self.__snd < 0:
            self.__fst = -self.__fst
            self.__snd = abs(self.__snd)
        return self

    def __str__(self):
        return f'{self.__fst}/{self.__snd}'

    def __repr__(self):
        return f"Fraction('{self.__fst}/{self.__snd}')"

    def numerator(self, *args):
        if len(args):
            self.__fst = args[0] * self.__sigh()
        self.__reduction()
        return abs(self.__fst)

    def denominator(self, *args):
        if len(args):
            self.__snd = args[0]
        self.__reduction()
        return abs(self.__snd)

    def __sigh(self):
        if self.__fst < 0:
            return -1
        else:
            return 1

    def __neg__(self):
        return Fraction(-self.__fst, self.__snd)