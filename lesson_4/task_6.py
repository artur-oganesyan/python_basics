from itertools import count
from itertools import cycle
from itertools import islice

i = 0
for el in cycle([el for el in islice(count(5), 5)]):
    if i >= 15:
        break
    print(el)
    i += 1
