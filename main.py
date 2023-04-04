# Cafeteria project : Create an live menu and payment system (a.k.a console program) :

#     Providing your full name the program should ask if table was reserved/not on spefic time or date.
#     And then if not program would assign you a table (there is a specific number single, double or family tables) .
#     After table is assigned to you, system should show how many free tables are and how which are reserved.
#     The system must be able to show name/surname of the person of the reserved table (CLI option : enter reserved table nuber ; OUTCOME: Name/Surname/Time Reserved)
#     After assigning table, system should show different menu options for breakfast, lunch , dinner , drinks (alcohol. alcohol free), to choose from. Special menu for vegetarian and vegan must be included too in the special menu. All menu items should have weight, preparation time in minutes, calories, and price.
#     I have to have an option to change the order before the payment section. Thus I can delete, add more, update amount of the same order.
#     I should be able to choose whatever I want from all menus in one ordering. After I finish, I need to see what I chosen, the full payable amount and approx waiting time for the food to be served
#     Add an option to add tips (% from the full cost) to the final bill.
#     After the payment , system should generate the receipt (logging).

# Steps:
# Create list of tables types and quantity (single, double, for family
# # Create meniu (maybe dictionary with meals and prices)
# #
# rezervacija, stalas, reserve/ne maistas gerimai


# import datetime
# from typing import List

# import pandas as pd

# tables = {
#     "Single": {
#         "Table_one": {"name": "Antanas", "status": "Reserved"},
#         "Table_two": {"name": "None", "status": "Available"},
#         "Table_tree": {"name": "None", "status": "Available"},
#         "Table_four": {"name": "None", "status": "Available"}},

#     "Double": {
#         "Table_one": {"name": "Paulius Dailidonis", "status": "Available"},
#         "Table_two": {"name": "Andrius Antanaitis", "status": "Reserved"},
#         "Table_tree": {"name": "None", "status": "Available"},
#         "Table_four": {"name": "None", "status": "Available"}},

#     "Family": {
#         "Table_one": {"name": "None", "status": "Available"},
#         "Table_two": {"name": "Jonas", "status": "Reserved"},
#         "Table_tree": {"name": "None", "status": "Available"},
#         "Table_four": {"name": "None", "status": "Available"}},
#     }


# client = input("Welcome to cafeteria. Please say Your name: ")

# # tables.get_values()

# for key, value in tables.items():
#     for key1, value1 in value.items():
#         for key2, value2 in value1.items():
#             if value2 == client:
#                 print(f"Your table {value1} is reserved for {client}")
#             if value2 != client:
#                 print("No table is reserved with this name")


# for key in tables.keys():
#     if client == tables.get(key):
# print(tables.get("name"))

# class Restaurant:
#     def __init__(self) -> None:
#         pass


# class Reservation:
#     def __init__(self, name: str, surname: str, time: datetime) -> None:
#         self.name = name
#         self.surname = surname
#         self.time = time


# class Table:
#     def __init__(self, number_of_seats: int):
#         self.number_of_seats = number_of_seats
#         self.reservations: List[Reservation] = []


#     def create_reservation(self, name: str, surname: str, time: datetime):

#         reservation = Reservation(name, surname, time)
#         self.reservations.append(reservation)

#     def check_availability(self, time: datetime) -> bool:
#         for reservation in self.reservations:
#             if reservation.time == time:
#                 return False
#         return True


# class Meniu:
#      def __init__(self):
#         pass

#      def get_meniu():
#         pass

#      def put_order():
#         pass


table_reservation = {
    "Table_one": {
        "Name": "Antanas",
        "Surname": "Antanėlis",
        "Time": "16:00",
        "Size": "Single",
    },
    "Table_two": {
        "Name": "Jonas",
        "Surname": "Jonelis",
        "Time": "18:00",
        "Size": "Double",
    },
    "Table_three": {
        "Name": "Petras",
        "Surname": "Petraitis",
        "Time": "19:30",
        "Size": "Family",
    },
    "Table_four": {"Name": "", "Surname": "", "Time": "", "Size": "Single"},
    "Table_four": {"Name": "", "Surname": "", "Time": "", "Size": "Double"},
    "Table_four": {"Name": "", "Surname": "", "Time": "", "Size": "Family"},
}

# rezervacijos informacija
name = input("Enter your name: ")
surname = input("Enter your surname: ")
time = input("Enter reservation time. Please enter time like 18:00 or 17:30): ")
table_size = input("Enter table size (Single, Double or Family): ")

# tikrinam ar stalas užrezervuotas
for table, reservation in table_reservation.items():
    if (
        reservation["Name"] == name
        and reservation["Surname"] == surname
        and reservation["Time"] == time
    ):
        print(
            f"Hello {name} {surname}, Your table is reserved for You at {time}. Please take your seats and choose from meniu"
        )
        break  # čia kažkaip reikės paduoti meniu kad rinktusi
else:
    # jei stalas nerezervuotas siūlo pasirinkti stalą
    available_table = ""
    for table, reservation in table_reservation.items():
        if reservation["Size"] == table_size and reservation["Name"] == "":
            available_table = table
            break

    if available_table == "":
        print(
            f"Sorry, there are no reservation for {name} {surname}. Would you like to reserve a table?"
        )
        response = input("Enter 'Yes' or 'No': ")
        if response.lower() == "yes":
            print("Great! Available tables sizes are: Single, Double and Family.")
            table_size = input("Enter table size: ")
            for table, reservation in table_reservation.items():
                if reservation["Size"] == "table_size" and reservation["Name"] == "":
                    available_table = table
                    break
            else:
                print(f"Sorry, no {table_size} tables are available.")
        else:
            print("Table not reserved.")
            available_table = ""

    # jei stalas neuzimtas rezervuoja
    if available_table is not None:
        table_reservation[available_table] = {
            "Name": name,
            "Surname": surname,
            "Time": time,
            "Size": table_size,
        }
        print(
            f"Table {available_table} ({table_size}) reserved for {name} {surname} at {time}."
        )
