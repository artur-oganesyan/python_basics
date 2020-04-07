values = [
    1,
    1.0,
    5 + 6j,
    'string',
    True,
    [0, 1, 2],
    (0, 1, 2),
    {0, 1, 2},
    {0: 1, 1: 2, 2: 3},
    b'\x00',
    bytearray(b'\x00\x01'),
    None
]

types = [
    int,
    float,
    complex,
    str,
    bool,
    list,
    tuple,
    set,
    dict,
    bytes,
    bytearray,
]

for i in values:
    for t in types:
        if type(i) == t:
            print(f'Type {i} is {t}')
            break
    else:
        print(f'Type for {i} is not found')
