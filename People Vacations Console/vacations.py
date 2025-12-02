from datetime import datetime, timedelta
import csv
import os

def get_employee_data(employee_id):
    ruta = os.path.join(os.path.dirname(__file__), "employees.csv")

    if not os.path.exists(ruta):
        return None

    with open(ruta, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader, None)
        for row in reader:
            if not row:
                continue
            if row[0] == employee_id:
                # row fields: id, name, position, area, contract_start_date, years_experience
                return {"id": row[0], "name": row[1], "start_contract": row[4]}

    return None


# ---------------------------
# time calculations
# ---------------------------
def calculate_months_worked(start_date):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    today = datetime.now()
    months = (today.year - start.year) * 12 + (today.month - start.month)
    if today.day < start.day:
        months -= 1
    return months


def calculate_available_days(start_date, employee_id):
    months = calculate_months_worked(start_date)
    accumulated_days = months * 1.5
    used_days = 0

    ruta = os.path.join(os.path.dirname(__file__), "vacations.csv")
    if os.path.exists(ruta):
        with open(ruta, mode="r", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader, None)
            for row in reader:
                if not row:
                    continue
                # vacations columns: employee_id, employee_name, start_date, end_date, days, status, month, year
                try:
                    if row[0] == employee_id and row[5].upper() == "APPROVED":
                        used_days += float(row[4])
                except (IndexError, ValueError):
                    # skip malformed rows
                    continue

    return accumulated_days - used_days


def count_days_without_sundays(start, end):
    try:
        d1 = datetime.strptime(start, "%Y-%m-%d")
        d2 = datetime.strptime(end, "%Y-%m-%d")
    except ValueError:
        return -1

    if d2 < d1:
        return -1

    count = 0
    current = d1
    while current <= d2:
        if current.weekday() != 6:  # Sunday
            count += 1
        current += timedelta(days=1)
    return count


# ---------------------------
# request vacation
# ---------------------------
def request_vacation():
    ruta = os.path.join(os.path.dirname(__file__), "vacations.csv")

    employee_id = input("Enter employee ID: ").strip()
    employee = get_employee_data(employee_id)
    if not employee:
        print(f"⚠ Employee with ID {employee_id} not found.")
        input("\n/---Press Enter to return---/")
        return

    name = employee["name"]
    start_contract = employee["start_contract"]

    start = input("Start vacation date (YYYY-MM-DD): ").strip()
    end = input("End vacation date (YYYY-MM-DD): ").strip()

    # validations on dates
    days = count_days_without_sundays(start, end)
    if days == -1:
        print("⚠ Invalid date(s) or wrong format (use YYYY-MM-DD).")
        input("\n/---Press Enter to return---/")
        return

    months = calculate_months_worked(start_contract)
    if months < 6:
        print("⚠ Employee has not completed 6 months.")
        input("\n/---Press Enter to return---/")
        return

    available = calculate_available_days(start_contract, employee_id)
    if days > available:
        print(f"⚠ Not enough days. Requested: {days}  —  Available: {available}")
        input("\n/---Press Enter to return---/")
        return

    # Save request
    try:
        with open(ruta, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            if os.stat(ruta).st_size == 0:
                writer.writerow(["employee_id", "employee_name", "start_date", "end_date", "days", "status", "month", "year"])
            now = datetime.now()
            writer.writerow([employee_id, name, start, end, days, "PENDING", now.month, now.year])
    except Exception as e:
        print("❌ Error saving vacation request:", e)
        input("\n/---Press Enter to return---/")
        return

    print("\n✅ Vacation request saved (PENDING)")
    input("\n/---Press Enter to return---/")


# ---------------------------
# list pending
# ---------------------------
def list_pending_requests():
    ruta = os.path.join(os.path.dirname(__file__), "vacations.csv")

    if not os.path.exists(ruta):
        print("\n❌ File 'vacations.csv' not found. No requests to display.")
        input("\n/---Press Enter to return---/")
        return

    with open(ruta, mode="r", encoding="utf-8") as file:
        rows = list(csv.reader(file))

    if len(rows) <= 1:
        print("\n✅ No vacation requests registered.")
        input("\n/---Press Enter to return---/")
        return

    pending_requests = [r for r in rows[1:] if len(r) > 5 and r[5].upper() == "PENDING"]

    if not pending_requests:
        print("\n✅ No pending requests found.")
        input("\n/---Press Enter to return---/")
        return

    print("""
 _________________________________________________________________________________
|                                                                                 |
|                                PENDING REQUESTS                                 |
|_________________________________________________________________________________|
""")
    print(f"{'No.':<4} | {'ID':<5} | {'Name':<30} | {'From':<12} | {'To':<12} | {'Days':<5}")
    print("-" * 85)

    for idx, row in enumerate(pending_requests, start=1):
        emp_id, name, start, end, days, status, month, year = row
        print(f"{idx:<4} | {emp_id:<5} | {name:<30} | {start:<12} | {end:<12} | {days:<5}")
        print("-" * 85)

    input("\n/---Press Enter to return---/")


# ---------------------------
# approve or reject
# ---------------------------
def approve_or_reject():
    ruta = os.path.join(os.path.dirname(__file__), "vacations.csv")

    if not os.path.exists(ruta):
        print("❌ File 'vacations.csv' not found.")
        input("\n/---Press Enter to return---/")
        return

    with open(ruta, mode="r", encoding="utf-8") as file:
        rows = list(csv.reader(file))

    pending_indices = []
    print("\nPENDING REQUESTS:\n")

    for i, row in enumerate(rows[1:], start=1):
        if len(row) > 5 and row[5].upper() == "PENDING":
            print(f"{len(pending_indices)+1}. {row[0]} | {row[1]} | {row[2]} → {row[3]} | {row[4]} days")
            pending_indices.append(i)

    if not pending_indices:
        print("No pending requests.")
        input("\n/---Press Enter to return---/")
        return

    # validate choice
    while True:
        choice_input = input(f"Choose number (1-{len(pending_indices)}) or press Enter to return: ").strip()
        if choice_input == "":
            return
        if not choice_input.isdigit():
            print("⚠ Enter a valid number.")
            continue
        choice = int(choice_input)
        if choice < 1 or choice > len(pending_indices):
            print("⚠ Number out of range.")
            continue
        break

    selected_row_idx = pending_indices[choice - 1]

    decision = input("Approve (A) or Reject (R): ").strip().upper()
    if decision not in ("A", "R"):
        print("⚠ Invalid decision. Use A or R.")
        input("\n/---Press Enter to return---/")
        return

    rows[selected_row_idx][5] = "APPROVED" if decision == "A" else "REJECTED"

    # Save back
    try:
        with open(ruta, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(rows)
    except Exception as e:
        print("❌ Error saving changes:", e)
        input("\n/---Press Enter to return---/")
        return

    if decision == "A":
        print("\n✅ Vacation APPROVED")
    else:
        print("\n❌ Vacation REJECTED")

    input("\n/---Press Enter to return---/")


# ---------------------------
# employee history
# ---------------------------
def employee_history():
    ruta = os.path.join(os.path.dirname(__file__), "vacations.csv")

    while True:
        employee_id = input("Enter employee ID for history (or press Enter to return): ").strip()
        if not employee_id:
            return
        employee = get_employee_data(employee_id)
        if not employee:
            print(f"⚠ Employee ID {employee_id} not found. Try again.")
            continue
        break

    if not os.path.exists(ruta):
        print("No vacation records.")
        input("\n/---Press Enter to return---/")
        return

    with open(ruta, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader, None)

        print("""
 __________________________________________________________________________________
|                                                                                  |  
|                                Vacation history                                  | 
|__________________________________________________________________________________|
""")
        print(f"{'Name':<30} | {'Start':<12} | {'End':<12} | {'Days':<5} | {'Status':<10}")
        print("-" * 80)

        found = False
        for row in reader:
            if len(row) < 6:
                continue
            if row[0] == employee_id:
                print(f"{row[1]:<30} | {row[2]:<12} | {row[3]:<12} | {row[4]:<5} | {row[5]:<10}")
                print("-" * 80)
                found = True

        if not found:
            print("No records.")

    input("\n/---Press Enter to return---/")
