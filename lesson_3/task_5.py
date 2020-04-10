def my_funk():
    """
    Requests a some numbers separated by a space and print their sum.
    If continue to enter, the new numbers are summed up with the previous result.
    If the value contain other symbol, all the numbers in front of it will be summed and a function completed.
    """
    my_list = []
    while True:
        new_list = input("Enter some numbers separated by a space: ").split(" ")
        try:
            for i in new_list:
                i = int(i)
                my_list.append(i)
        except ValueError:
            break
        print(sum(my_list))
    print(sum(my_list))


my_funk()
