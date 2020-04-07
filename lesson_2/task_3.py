seasons_list = ['winter', 'spring', 'summer', 'autumn']
seasons_dict = {0: 'winter', 1: 'spring', 2: 'summer', 3: 'autumn'}

while True:
    month = int(input('Enter the month number: '))
    if 1 <= month <= 12:
        if 1 <= month <= 2 or month == 12:
            season = 0
        elif 3 <= month <= 5:
            season = 1
        elif 6 <= month <= 8:
            season = 2
        elif 9 <= month <= 11:
            season = 3
        # List
        print(seasons_list[season])
        # Dict
        print(seasons_dict.get(season))
        break
    else:
        print('Month with this number does not exist. Try again')
        continue
