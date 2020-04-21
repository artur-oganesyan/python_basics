try:
    with open("text_2.txt", "r+") as file:
        file.write(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit,"
            " sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\n"
            "Nisi vitae suscipit tellus mauris a.\n"
            "Rutrum quisque non tellus orci ac.\n"
            "Pellentesque id nibh tortor id.\n"
            "Non diam phasellus vestibulum lorem.\n"
            "Eget magna fermentum iaculis eu non diam.\n"
            "Felis imperdiet proin fermentum leo vel orci porta non pulvinar.")
        file.seek(0)
        lines = file.readlines()
        print(f"File contain {len(lines)} lines.")
        for i, l in enumerate(lines, start=1):
            print(f"Line {i}, contain {len(l.split())} words: {l}", end="")
except IOError:
    print("Error")
