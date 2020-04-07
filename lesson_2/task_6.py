items = []
indicators = {}
count = 1
while True:
    name = input('Enter item name: ')
    price = input('Enter price: ')
    amount = input('Enter amount: ')
    unit = input('Enter unit: ')
    items.append((count, {'name': name, 'price': price, 'amount': amount, 'unit': unit}))
    is_more = input('Add more? Yes or Not: ').lower()
    if is_more == 'y' or is_more == 'yes':
        count += 1
        continue
    else:
        break
for item_tuple in items:
    item = item_tuple[1]
    for k, v in item.items():
        index_list = []
        index_list.append(v)
        if indicators.get(k):
            indicators[k].append(index_list.pop(0))
        else:
            indicators.update({k: index_list})
print(indicators)
