import json
try:
    companies = {}
    with open("text_7.txt") as file:
        for line in file:
            name, opf, revenue, costs = line.split()
            profit = int(revenue) - int(costs)
            companies[name] = profit

    profitable_companies = {k: v for k, v in companies.items() if v > 0}
    average_profit = sum(profitable_companies.values()) / len(profitable_companies)
    data = [companies, {"average_profit": average_profit}]

    with open("text_77.json", 'w') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)

except IOError:
    print("Error")
