# ---------------------------------------------------------- #
# Title: Main
# Description: A main module for Assignment09
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# erikjk,5.12.2020,Added Code to Complete Assignment
# erikjk,5.12.2020,Outlined options, created global variables
# erikjk,5.12.2020,Filled in each menu choice with imported functions
# erikjk,5.13.2020,Added try/except to choice 2, removing it from IO Class
# erikjk,5.13.2020,Cleaning up and commenting, final debugging
# ---------------------------------------------------------- #

if __name__ == "__main__":
    from DataClasses import Employee as Emp
    from ProcessingClasses import FileProcessor as Fp
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")

# Data ----------------------------------------------------- #
lstOfEmployeeObjects = [] # A list of object rows
strFileName = "EmployeeData.txt" # The target file for reading/writing
strMenuChoice = "" # Captures user input for menu choice
objFile = None  # Object for opening/closing target file
objEmployee = None  # Object collecting user input data, 3 attributes

# Main Body of Script -------------------------------------- #
lstOfEmployeeObjects = Fp.read_data_from_file(strFileName)
print(lstOfEmployeeObjects)

# Show user a menu of options
while True:
    Eio.print_menu_items()

    # Get user's menu option choice
    strChoice = Eio.input_menu_options()

    # Show current employee data to user
    if strChoice.strip() == "1":
        Eio.print_current_list_items(lstOfEmployeeObjects)
        continue

    # Let user add new employee data
    if strChoice.strip() == "2":
        while True: # While loop prevents being kicked back to main menu during error
            try:
                objEmployee = Eio.input_employee_data()
                lstOfEmployeeObjects.append(objEmployee)
                print(objEmployee.first_name + " " +
                      objEmployee.last_name +
                      " has been added with Employee ID #" +
                      str(objEmployee.employee_id) + "\n",
                      type(objEmployee))
            except Exception as e:
                print("\n", e, "\n")
                print("\t** Error - Cannot Create Employee **\n")
            except UnboundLocalError:
                print() # Add line for looks
                print("\t** Error - Cannot Create Employee **\n")
            finally:
                break
        continue

    # Let user save employee data to file
    if strChoice.strip() == "3":
        Fp.save_data_to_file(strFileName, lstOfEmployeeObjects)
        continue

    # Let user exit program
    if strChoice.strip() == "4":
        print("Employees Ahoy!")
        break

    else:
        print("\t** \"" + str(strChoice) + "\" is not a vaild option **")

