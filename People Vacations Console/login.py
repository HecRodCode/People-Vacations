import csv
import os
import utils

def login_menu():
    print("""
 ________________________________________
|                                        |
|           PeopleOps Vacations          |
|________________________________________|
|                                        |
|   >> Username:                         |
|   >> Password:                         |                                    
|   >> Rol:                              |
|________________________________________| 
""")

def login_admin(attempts=1, limit=3):
    utils.restart()
    login_menu()

    print(f"Intento: {attempts} de {limit}")

    username = input("Enter your username:")
    password = input("Enter your password:")

    ruta_csv = os.path.join(os.path.dirname(os.path.abspath(__file__)), "users.csv")

    try:
        with open(ruta_csv, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row["user"] == username and row["password"] == password:
                    return True
    except FileExistsError:
        print("ERROR: The file was not found (user,csv)")
        return True
    
    print("Incorrect username or password.")

    if attempts >= limit:
        return False
    
    return login_admin(attempts+1,limit)