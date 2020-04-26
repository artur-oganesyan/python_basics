import json


class Warehouse:
    def __init__(self):
        self.db_name = "warehouse.json"
        try:
            with open(self.db_name) as file:
                self.data = json.load(file)
        except IOError:
            print("Read error a file", self.db_name)

    def __write(self):
        try:
            with open(self.db_name, "w") as file:
                json.dump(self.data, file, indent=4, ensure_ascii=False)
        except IOError:
            print("Write error it file", self.db_name)

    def receive(self, item):
        item_params = item.__dict__
        search_item = self.find(item_params["serial_number"])
        if not search_item:
            self.data.setdefault(item_params["equipment_type"], []).append(item_params)
            self.__write()
        else:
            print(f'{search_item["equipment_type"]} with serial number: "{search_item["serial_number"]}" exist in warehouse.')

    def give_out(self, serial_number):
        search_item = self.find(serial_number)
        if search_item:
            self.data.get(search_item["equipment_type"]).remove(search_item)
            self.__write()
            return search_item
        else:
            print(f'Item with serial number: "{serial_number}" not found in warehouse.')

    def find(self, serial_number):
        for items_list in self.data.values():
            temp_list = list(filter(lambda i: i["serial_number"] == serial_number, items_list))
            if temp_list:
                if len(temp_list) > 1:
                    print("Found few items with this SN, check DB")
                return temp_list[0]

    def indicators(self):
        for item_type, items_list in self.data.items():
            print(f"{item_type}s: {len(items_list)}")


class OfficeEquipment:
    def __init__(self, equipment_type, brand, model, serial_number, ):
        self.equipment_type = equipment_type
        self.brand = brand
        self.model = model
        self.serial_number = serial_number


class Printer(OfficeEquipment):
    def __init__(self, brand, model, serial_number, print_type, two_sided_printing):
        super().__init__(__class__.__name__, brand, model, serial_number)
        self.print_type = print_type
        self.two_sided_printing = two_sided_printing


class Scanner(OfficeEquipment):
    def __init__(self, brand, model, serial_number, scan_speed, resolutions):
        super().__init__(__class__.__name__, brand, model, serial_number)
        self.scan_type = scan_speed
        self.resolutions = resolutions


class Shredder(OfficeEquipment):
    def __init__(self, brand, model, serial_number, basket_volume, max_destroyed_sheets):
        super().__init__(__class__.__name__, brand, model, serial_number)
        self.basket_volume = basket_volume
        self.max_destroyed_sheets = max_destroyed_sheets


printer = Printer("HP", "sh01", "er3452", 12, 5)
shredder = Shredder("HP", "sh01", "sdfgs3414", 12, 5)

warehouse = Warehouse()
warehouse.receive(printer)
warehouse.receive(shredder)
warehouse.give_out("hbfgd435sd")
warehouse.give_out("sf42gfs")
print(warehouse.find("sdfgs3414"))
