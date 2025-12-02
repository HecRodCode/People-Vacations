import os
import csv

def export_vacation_report():
    """
    Exporta un reporte de solicitudes de vacaciones para un mes y año específicos.
    Genera un CSV y lo imprime en consola con estilo tabla.
    """

    vacations_path = os.path.join(os.path.dirname(__file__), "vacations.csv")
    employees_path = os.path.join(os.path.dirname(__file__), "employees.csv")

    # Validar existencia de archivos
    if not os.path.exists(vacations_path):
        print("⚠ No existe el archivo 'vacations.csv'.")
        input("\n/---Press Enter to return to the main menu---/")
        return
    if not os.path.exists(employees_path):
        print("⚠ No existe el archivo 'employees.csv'.")
        input("\n/---Press Enter to return to the main menu---/")
        return

    # Pedir mes y año al usuario
    try:
        month = int(input("Ingrese el número del mes (1-12): "))
        year = int(input("Ingrese el año (YYYY): "))
        if month < 1 or month > 12:
            print("⚠ Mes inválido.")
            input("\n/---Press Enter to return to the main menu---/")
            return
    except ValueError:
        print("⚠ Mes o año inválido.")
        input("\n/---Press Enter to return to the main menu---/")
        return

    # Leer empleados para obtener datos de nombre completo si es necesario
    employees_data = {}
    with open(employees_path, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader, None)
        for row in reader:
            emp_id, name, *_ = row
            employees_data[emp_id] = name

    # Leer solicitudes de vacaciones y filtrar por mes y año
    filtered = []
    with open(vacations_path, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        header = next(reader, None)

        for row in reader:
            try:
                row_month = int(row[6])
                row_year = int(row[7])
            except ValueError:
                continue  # Saltar filas corruptas
            if row_month == month and row_year == year:
                filtered.append(row)

    if not filtered:
        print(f"\n⚠ No hay solicitudes de vacaciones para {month}/{year}.")
        input("\n/---Press Enter to return to the main menu---/")
        return

    # Crear archivo CSV de salida
    output_file = os.path.join(os.path.dirname(__file__), f"vacation_report_{year}_{month}.csv")
    with open(output_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(filtered)

    # Imprimir reporte en consola
    print(f"\n✅ Reporte de solicitudes de vacaciones para {month}/{year}")
    print("-"*105)
    print(f"{'ID':<5} | {'Nombre':<30} | {'Inicio':<12} | {'Fin':<12} | {'Días':<5} | {'Estado':<10} | {'Mes':<3} | {'Año':<4}")
    print("-"*105)

    for row in filtered:
        emp_id, name, start, end, days, status, row_month, row_year = row
        # Si el nombre no está en el CSV de vacations, tomarlo de employees
        if not name.strip() and emp_id in employees_data:
            name = employees_data[emp_id]
        print(f"{emp_id:<5} | {name:<30} | {start:<12} | {end:<12} | {days:<5} | {status:<10} | {row_month:<3} | {row_year:<4}")
        print("-"*105)

    print(f"\nArchivo generado correctamente: {output_file}\n")
    input("\n/---Press Enter to return to the main menu---/")
