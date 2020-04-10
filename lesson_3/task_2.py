def user_data(name, surname, year, city, email, phone):
    """Print user data in one line"""
    print(f"User data: name: {name}, surname: {surname}, year: {year}, city: {city}, phone: {phone}, email: {email}")


user_data(
    name=input("Enter name: "),
    surname=input("Enter surname: "),
    phone=input("Enter phone: "),
    email=input("Enter email: "),
    city=input("Enter city: "),
    year=input("Enter year: ")
)
