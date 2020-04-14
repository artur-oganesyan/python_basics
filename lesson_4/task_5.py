import functools

print(functools.reduce(lambda prev_el, el: prev_el * el, [el for el in range(100, 1001)]))
