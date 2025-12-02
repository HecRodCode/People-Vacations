import menu 
import utils
import login
import employees
import vacations
import reports

while True:
    utils.restart()
    access = login.login_admin()

    if access == False:
        print("\nAccess denied")
        break

    while True:
        utils.restart()
        menu.main_menu()

        option = utils.validation_data("Chosee an option:",1,4)

        match option:
            case 1:
                while True:
                    utils.restart()
                    menu.employees_menu()

                    option = utils.validation_data("Chosse an option: ",1,6)

                    match option:
                        case 1:
                            while True:
                                utils.restart()
                                menu.register_employees()

                                id = input("Enter the employee ID:")
                                name = input("Enter the employee name:")
                                position = input("Enter the employee position:")
                                area = input("Enter de employee area:")
                                start_contract = input("Enter the start date of the employee's contract (YYYY-MM-DD):")
                                years_experience = input("Enter the employee's years of experience:")

                                employees.register_employees(id,name,position,area,start_contract,years_experience)
                                break
                        case 2:
                            while True:
                                utils.restart()
                                employees.show_employees()
                                break
                        case 3:
                            while True:
                                utils.restart()
                                employees.search_employee()
                                break
                        case 4:
                            while True:
                                utils.restart()
                                employees.update_data_employee()
                                break
                        case 5:
                            while True:
                                utils.restart()
                                employees.delete_employee()
                                break
                        case 6:
                            break
            case 2:
                while True:
                    utils.restart()
                    menu.vacations_menu()

                    option = utils.validation_data("Chosse a option: " ,1,5)

                    match option:
                        case 1:
                            while True:
                                utils.restart()
                                vacations.request_vacation()
                                break
                        case 2:
                            while True:
                                utils.restart()
                                vacations.list_pending_requests()
                                break
                        case 3:
                            while True:
                                utils.restart()
                                vacations.approve_or_reject()
                                break
                        case 4:
                            while True:
                                utils.restart()
                                vacations.employee_history()
                                break
                        case 5:
                            break
            case 3:
                while True:
                    utils.restart()
                    reports.export_vacation_report()
                    break
            case 4:
                while True:
                    utils.restart()
                    menu.farewell_menu()
                    exit()
