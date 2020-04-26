class NumericError(Exception):
    def __init__(self, text):
        self.text = text


result = []
while True:
    el = input('Enter value for append in list (enter "stop" for finish): ')
    if el.lower() == "stop":
        break
    try:
        if el.isnumeric():
            result.append(el)
        else:
            raise NumericError("Value should be a number")
    except NumericError as err:
        print(err)
print(result)



