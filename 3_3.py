# A
[num ** 2 for num in range(a, b + 1)]

# b
[[x * i for x in range(1, n + 1)] for i in range(1, n + 1)]

# c
[len(slovo) for slovo in sentence.split()]
# d
{num for num in numbers if num % 2 == 1}
# e
{num for num in numbers if num in [number ** 2 for number in range(1, int(max(numbers) ** 0.5 + 1))]}