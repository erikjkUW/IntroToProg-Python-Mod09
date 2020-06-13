# ---------------------------------------------------------- #
# Title: IO Classes
# Description: A module of IO classes
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# erikjk,5.13.2020,Edited input_employee_data
# erikjk,5.13.2020,Cleaning up and commenting
# ---------------------------------------------------------- #
if __name__ == "__main__":
    raise Exception("This file is not meant to ran by itself")
else: 
    import DataClasses as DC

class EmployeeIO:
    """  A class for performing Employee Input and Output

    methods:
        print_menu_items():

        print_current_list_items(list_of_rows):

        input_employee_data():

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class:
        erikjk,5.13.2020,Removed try/except from input_employee_data():
        erikjk,5.13.2020,Called DataClasses explicitly in input_employee_data():
    """
    @staticmethod
    def print_menu_items():
        """ Print a menu of choices to the user  """
        print('''
        Menu of Options
            1) Show current employee data
            2) Add new employee data
            3) Save employee data to File
            4) Exit program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_options():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_list_items(list_of_rows: list):
        """ Print the current items in the list of Employee rows

        :param list_of_rows: (list) of rows you want to display
        """
        print("******* The current items employees are: *******")
        for row in list_of_rows:
            print(str("ID #" + row.employee_id)
                  + " - "
                  + row.first_name
                  + " "
                  + row.last_name)
        print("************************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_employee_data():
        """ Gets data for a employee object

        :return: (employee) object with input data
        """
        emp = DC.Employee("","","") # Initialize object
        emp.employee_id = input("What is the employee Id? - ").strip()
        emp.first_name = input("What is the employee First Name? - ").strip()
        emp.last_name = input("What is the employee Last Name? - ").strip()
        print()  # Add an extra line for looks

        return emp

