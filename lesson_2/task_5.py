rating = [7, 5, 3, 3, 2]
print('Current rating:', rating)
rate = int(input('Enter new rate: '))
rating.append(rate)
rating.sort(reverse=True)
print(rating)
