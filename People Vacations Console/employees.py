import utils
import os
import csv

def register_employees(id, name, position, area, start_contract, years_experience):
    if not utils.validation_id(id): 
        return
    if not utils.validation_name(name): 
        return
    if not utils.validation_date(start_contract): 
        return
    if not utils.validation_years_experience(years_experience): 
        return

    ruta_csv = os.path.join(os.path.dirname(__file__), "employees.csv")

    with open(ruta_csv, mode="a", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)

        if os.stat(ruta_csv).st_size == 0:
            writer.writerow(["id", "name", "position", "area", "contract_start_date", "years_experience"])

        writer.writerow([id, name, position, area, start_contract, years_experience])

    print("\n✅ Employee added correctly!")

def show_employees():
    ruta_csv = os.path.join(os.path.dirname(__file__), "employees.csv")

    with open(ruta_csv, "r", encoding="utf-8",) as file:
        reader = csv.reader(file)
        lines = list(reader)

    if len(lines) <= 1:
        print("""
 ____________________________________________________
|                                                    |
|         ¡There are no registered employees!        |
|____________________________________________________|
""")
        input("\n/---Press Enter to return to the main menu---/")
        return
    
    print("""
 _________________________________________________________________________________________________________________________________________
|                                                                                                                                         |
|                                                  List of employees                                                                      |
|_________________________________________________________________________________________________________________________________________| 
""")
    print(f"{'ID':<5} | {'Name':<40} | {'Position':<30} | {'Area':<20} | {'Date of hire':<15} | {'Years of experience':<2}")
    print("-" * 135)

    for row in lines[1:]:
        id,name,position,area,start_contract,years_experience = row
        print(f"{id:<5} | {name:<40} | {position:<30} | {area:<20} | {start_contract:<15} | {years_experience:<2} ")
        print( "-" * 135)
    
    input("\n/---Press Enter to return to the employees menu---/")
    return

def search_employee():
    ruta_csv = os.path.join(os.path.dirname(__file__), "employees.csv")

    with open(ruta_csv, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        lines = list(reader)

    if len(lines) <= 1:
        print("""
 ____________________________________________________
|                                                    |
|         ¡There are no registered employees!        |
|____________________________________________________|
""")
        input("\n/---Press Enter to return to the employees menu---/")
        return
    
    id_employee = input("Enter the employee ID:")
    found = False

    for row in lines [1:]:
        id,name,position,area,start_contract,years_experience = row
        if id == id_employee:
            print("""
 ________________________________________________________________________________________________________________________________
|                                                                                                                                |
|                                                  Employee found                                                                |
|________________________________________________________________________________________________________________________________| 
""")
            print(f"{'ID':<5} | {'Name':<30} | {'Position':<30} | {'Area':<15} | {'Date of hire':<15} | {'Years of experience':<2}")
            print("-" * 130)

            print(f"{id:<5} | {name:<30} | {position:<30} | {area:<15} | {start_contract:<15} | {years_experience:<2} ")
            print( "-" * 130)
            found = True
            break
    if not found:
        print(f"No employee with this ID was found: {id_employee}")
    input("\n/---Press Enter to return to the employees menu---/")
    return

def update_data_employee():
    ruta_csv = os.path.join(os.path.dirname(__file__), "employees.csv")

    with open(ruta_csv,"r", encoding="utf-8") as file:
        reader = csv.reader(file)
        rows = list (reader)

    if len(rows) <= 1:
        print("""
 ____________________________________________________
|                                                    |
|         ¡There are no registered employees!        |
|____________________________________________________|
""")
        input("\n/---Press Enter to return to the employees menu---/")
        return
    
    id_employee = input("Enter the ID of the employee you want to update:")
    found = False

    for i, row in enumerate(rows[1:], start=1):
        id,name,position,area,start_contract,years_experience = row
        if id == id_employee:
            print("""
 ________________________________________________________________________________________________________________________________
|                                                                                                                                |
|                                                  Employee found                                                                |
|________________________________________________________________________________________________________________________________| 
""")
            print(f"{'ID':<5} | {'Name':<30} | {'Position':<30} | {'Area':<15} | {'Date of hire':<15} | {'Years of experience':<2}")
            print("-" * 130)

            print(f"{id:<5} | {name:<30} | {position:<30} | {area:<15} | {start_contract:<15} | {years_experience:<2} ")
            print( "-" * 130)

            print("\n/---If you do not want to change anything - Press Enter---/")

            new_name = input(f"\nEnter the new name [{name}]:") or name
            new_position = input(f"\nEnter the new position [{position}]:") or position
            new_area = input(f"\nEnter the new area [{area}]:") or area
            new_date = input(f"\nEnter the new contract date [{start_contract}]:") or start_contract
            new_years = input(f"\nenter years of experience [{years_experience}]:") or years_experience

            rows[i] = [id,new_name,new_position,new_area,new_date,new_years]
            found = True
            break

    if not found:
        print(f"No employee with this ID was found: {id_employee}")
        input("\n/---Press Enter to return to the employees menu---/")
        return
    
    with open(ruta_csv, "w",newline="",encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print("\nCorrectly updated employee data")
    input("\n/---Press Enter to return to the employees menu---/")
    return

def delete_employee():
    ruta_csv = os.path.join(os.path.dirname(__file__), "employees.csv")

    with open(ruta_csv,"r",encoding="utf-8",newline="") as file:
        reader = csv.reader(file)
        rows = list(reader)
    
    if len(rows) <= 1:
        print("""
 ____________________________________________________
|                                                    |
|         ¡There are no registered employees!        |
|____________________________________________________|
""")
        input("\n/---Press Enter to return to the employees menu---/")
        return
    
    id_employee = input("Enter the ID of the employee you want to update:")
    found = False

    for i, row in enumerate(rows[1:], start=1):
        id,name,position,area,start_contract,years_experience = row
        if id == id_employee:
            print("""
 ________________________________________________________________________________________________________________________________
|                                                                                                                                |
|                                                  Employee found                                                                |
|________________________________________________________________________________________________________________________________| 
""")
            print(f"{'ID':<5} | {'Name':<30} | {'Position':<30} | {'Area':<15} | {'Date of hire':<15} | {'Years of experience':<2}")
            print("-" * 130)

            print(f"{id:<5} | {name:<30} | {position:<30} | {area:<15} | {start_contract:<15} | {years_experience:<2} ")
            print( "-" * 130)

            confirm = input("\n Are you sure want to delete this employee? (Yes / No)").lower()
            if confirm == "yes":
                rows.pop(i)
                found = True
                break
            else:
                input("\n/---Press Enter to return to the employees menu---/")
                return
            
    if not found:
        print(f"No employee with this ID was found: {id_employee}")
        input("\n/---Press Enter to return to the employees menu---/")
        return
    
    with open(ruta_csv,"w",encoding="utf-8",newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print("\nEmployee successfully deleted.")
    input("\n/---Press Enter to return to the employees menu---/")
    return