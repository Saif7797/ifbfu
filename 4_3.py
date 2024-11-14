# A
def recursive_sum(*nums):
    if not nums:
        return 0
    return nums[0] + recursive_sum(*nums[1:])
# b
def recursive_digit_sum(num):
    while num >= 10:
        return num % 10 + recursive_digit_sum(num // 10)
    return num
# c
def make_equation(*num):
    if len(num) == 1:
        return f'{num[0]}'
    else:
        return f'({make_equation(*num[:-1])}) * x + {num[-1]}'
# d
def answer(f):
    def code(*args, **kwargs):
        return f'Результат функции: {f(*args, ** kwargs)}'
    return code
# e
def result_accumulator(func):
    queue = []

    def wrapper(*args, method='accumulate', **kwargs):
        queue.append(func(*args, **kwargs))
        if method == 'drop':
            result = list(queue)
            queue.clear()
            return result
    return wrapper