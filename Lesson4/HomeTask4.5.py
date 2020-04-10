import random
from functools import reduce

result_list = reduce(lambda a, x: a*x, (random.choices([i for i in range(100, 1001)], k = 4)))
print(result_list)