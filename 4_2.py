# A
def make_list(length, value=0):
    return [value for _ in range(length)]
# b
def make_matrix(size, value=0):
    if type(size) is int:
        return [[value for i in range(size)] for j in range(size)]
    else:
        return [[value for i in range(size[0])] for j in range(size[1])]
# c
def gcd(*args):
    a = list(args)
    while len(a) > 1:
        while a[1]:
            a[0], a[1] = a[1], a[0] % a[1]
        a.pop(1)
    return a[0]
# d
def month(n, lang='ru'):
    months = {'en': ['0', 'January', 'February', 'March', 'April', 'May', 'June',
                     'July', 'August', 'September', 'October', 'November', 'December'],
              'ru': ['0', 'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
                     'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']}
    return months[lang][n]
# e
def to_string(*data, sep=' ', end='\n'):
    string = ''
    data = list(data)
    while data:
        item = data.pop(0)
        string += str(item)
        if data:
            string += sep
    return string + end