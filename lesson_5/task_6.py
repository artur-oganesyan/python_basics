try:
    lessons = dict()
    with open("text_6.txt") as file:
        for line in file:
            name, *les_types = line.split()
            s = list()
            for les_type in les_types:
                n = ("".join(el for el in les_type if el.isdigit()))
                if n:
                    s.append(int(n))
            lessons[name[:-1]] = sum(s)
    print(lessons)
except IOError:
    print("Error")
