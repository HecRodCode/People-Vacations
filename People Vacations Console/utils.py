import os
import re
import csv
from datetime import datetime

def restart():
    os.system("cls" if os.name == "nt" else "clear")

def validation_data(message, minimum, maximum):
    while True:
        opcion = input(message)

        if not opcion.isdigit():
            print("⚠ Error: You must enter a number..")
            continue

        opcion = int(opcion)

        if opcion < minimum or opcion > maximum:
            print(f"⚠ Error: Ingresa un número entre {minimum} y {maximum}.")
            continue
        return opcion

def validation_id(id):
    if not id.strip():
        print("⚠ ID cannot be empty.")
        return False

    if not id.isdigit():
        print("⚠ ID must contain only numbers.")
        return False

    return True

def validation_name(name):
    if name.strip() == "":
        print("⚠ The name cannot be empty.")
        return False

    if not all(x.isalpha() or x.isspace() for x in name):
        print("⚠ The name should only contain letters and spaces.")
        return False
    return True

def validation_date(start_contract):
    try:
        date_obj = datetime.strptime(start_contract, "%Y-%m-%d")

        if date_obj > datetime.now():
            print("⚠ Start date cannot be in the future.")
            return False

        return True
    except ValueError:
        print("⚠ Invalid date format. Use YYYY-MM-DD.")
        return False

def validation_years_experience(years_experience):
    if not years_experience.isdigit():
        print("⚠ Years of experience must be a number.")
        return False

    years_experience = int(years_experience)

    if years_experience < 0 or years_experience > 60:
        print("⚠ Invalid years of experience.")
        return False

    return True
