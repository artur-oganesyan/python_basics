try:
    with open("text_3.txt") as file:
        lines = file.readlines()
        sum_salaries = float()
        employees = list()
        for line in lines:
            salary = float(line.split()[1])
            if salary < 20000:
                employees.append(line.split()[0])
            sum_salaries += salary
        print("Employees with a salary of less than 20,000:", ", ".join(employees))
        print("Average salary of all employees:", sum_salaries / len(lines))
except IOError:
    print("Error")
