from sys import argv

try:
    script_name, hour, rate, premium = argv
    print("Salary:", (int(hour) * int(rate)) + int(premium))
except ValueError:
    print("Enter only three number variables: hour, rate and premium")
