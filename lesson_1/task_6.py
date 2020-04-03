distance = int(input("Enter distance in first day: "))
required_distance = int(input('Enter required distance: '))

day = 1
while True:
    if distance >= required_distance:
        print(f'On {day} day you achieve required distance in {required_distance} km')
        break
    day += 1
    distance *= 1.1
