from itertools import product

nums = [0, 4, 3, 0]
target = 7
ls = list(filter(lambda x: x < target and x != 0, nums))
print(list(product(ls, repeat=2)))
