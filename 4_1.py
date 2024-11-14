# A
def print_hello(name):
    print(f'Hello, {name}!')

# b
def gcd(a, b):
    while a != 0 and b != 0:
        if a >= b:
            a -= b
        else:
            b -= a
    return (a + b)
# c
def number_length(a):
    count = 0
    while a != 0:
        if a < 0:
            a *= -1
        a = int(a // 10)
        count += 1
    return count
#на каком то 23 тесте что то идет не по плану, но 22 отыгрывает прекрасно, понятия не имею что там за тест, но без встроенных функций не знаю что еще сделать
# d
def month(n, lang):
    months = {'en': ['0', 'January', 'February', 'March', 'April', 'May', 'June',
                     'July', 'August', 'September', 'October', 'November', 'December'],
              'ru': ['0', 'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
                     'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']}
    return months[lang][n]
# e
def split_numbers(string):
    return tuple([int(number) for number in string.split()])