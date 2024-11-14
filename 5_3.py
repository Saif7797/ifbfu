# A
try:
    func()
except ValueError:
    print('ValueError')
except TypeError:
    print('TypeError')
except SystemError:
    print('SystemError')
else:
    print('No Exceptions')
# b
try:
    func('2', None)
except ValueError:
    print('Ура! Ошибка!')
# c
class Problem:

    def __repr__(self):
        raise Exception


try:
    a = Problem()
    func(a)
except ValueError:
    print('Ура! Ошибка!')

# d
def only_positive_even_sum(*args):
    for i in args:
        if not isinstance(i, int):
            raise TypeError
        elif i <= 0 or i % 2 != 0:
            raise ValueError
    return sum(args)
# e
def check_queue_iterated(*queues):
    for queue in queues:
        try:
            iter(queue)
        except TypeError:
            raise StopIteration


def check_queue_consistence(*queues):
    queue = []
    for queue_in_queues in queues:
        queue.extend(list(queue_in_queues))
    if not all(type(member) is type(queue[0]) for member in queue):
        raise TypeError


def check_queue_sorted(*queues):
    for queue in queues:
        if list(queue) != sorted(queue):
            raise ValueError
    return True


def merge(queue_1, queue_2):
    check_queue_iterated(queue_1, queue_2)
    check_queue_consistence(queue_1, queue_2)
    check_queue_sorted(queue_1, queue_2)
    queue_1n = list(queue_1)
    queue_2n = list(queue_2)
    sequence = []

    while queue_1n and queue_2n:
        if queue_1n[0] > queue_2n[0]:
            sequence.append(queue_2n.pop(0))
        else:
            sequence.append(queue_1n.pop(0))
    sequence.extend(queue_1n + queue_2n)
    return sequence
