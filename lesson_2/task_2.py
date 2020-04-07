values_list = list(input('Enter values to create a list: '))
for i in range(0, len(values_list) - 1, 2):
    first_value, second_value = values_list[i], values_list[i + 1]
    values_list[i], values_list[i + 1] = second_value, first_value
print(values_list)
