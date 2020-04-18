try:
    with open("text_1.txt", "w") as file:
        while True:
            data = input("Enter a sentence: ")
            if not data:
                break
            print(data, file=file)
except IOError:
    print("Error")
