import random

data = [str(random.randint(1, 100)) for el in range(50)]

with open("text_5.txt", "r+") as file:
    file.write(" ".join(data))
    file.seek(0)
    content = file.read()
    list_int = list(map(int, content.split()))
    print(sum(list_int))
