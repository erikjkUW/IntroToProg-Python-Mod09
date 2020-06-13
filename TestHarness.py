# ---------------------------------------------------------- #
# Title: TestHarness
# Description: A main module for testing
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# erikjk,5.12.2020,Added Code to Complete Assignment
# erikjk,5.13.2020,Used TestHarness to raise exceptions - didn't work
# erikjk,5.13.2020,
# ---------------------------------------------------------- #
# CODE FROM PREVIOUS TESTS - IGNORE #
"""
if __name__ == "__main__":
    from DataClasses import Employee as Emp
    from ProcessingClasses import FileProcessor as Fp
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")

# Test data module
objP1 = Emp(1, "Bob", "Smith")
objP2 = Emp(2, "Sue", "Jones")
lstTable = [objP1, objP2]
for row in lstTable:
    print(row.to_string(), type(row))

# Test processing module
Fp.save_data_to_file("EmployeeData.txt", lstTable)
lstFileData = Fp.read_data_from_file("EmployeeData.txt")
lstTable.clear()
for line in lstFileData:
    lstTable.append(Emp(line[0], line[1], line[2].strip()))
for row in lstTable:
    print(row.to_string(), type(row))

# Test IO classes
Eio.print_menu_items()
Eio.print_current_list_items(lstTable)
print(Eio.input_employee_data())
print(Eio.input_menu_options())
"""
# CODE FROM PREVIOUS TESTS - IGNORE #

class Employee(object): # Testing exception handling with single class of objects

    def __init__(self, employee_id, first_name, last_name):
        # Attributes
        self.__first_name = first_name
        self.__last_name = last_name
        self.__employee_id = employee_id

    # --Properties--
    @property
    def first_name(self):
        return str(self.__first_name).title()

    @first_name.setter
    def first_name(self, value):
        if not str(value).isnumeric():
            self.__first_name = value
        else:
            raise Exception("Names cannot be numbers")

    @property
    def last_name(self):
        return str(self.__last_name).title()

    @last_name.setter
    def last_name(self, value):
        if not str(value).isnumeric():
            self.__last_name = value
        else:
            raise Exception("Names cannot be numbers")

    @property
    def employee_id(self):
        return self.__employee_id

    @employee_id.setter
    def employee_id(self, value):
        if not value.isalpha(): # Exception only triggers when the IO method calls the class
            self.__employee_id = value
        else:
            raise Exception("IDs must be numbers")

    # -- Methods --
    def to_string(self):
        """ Explicitly returns a string with this object's data """
        return self.__str__()

    def __str__(self):
        """ Implicitly returns a string with this object's data """
        return str(self.employee_id) + ',' + self.first_name + ',' + self.last_name

class IO():
    @staticmethod
    def input_employee_data():
        """ Gets data for a employee object

        :return: (employee) object with input data
        """
        emp = Employee("","","")
        emp.employee_id = input("What is the employee Id? - ").strip() # must have emp.x to work
        emp.first_name = str(input("What is the employee First Name? - ").strip())
        emp.last_name = str(input("What is the employee Last Name? - ").strip())
        print()  # Add an extra line for looks
        emp = Employee(employee_id,first_name,last_name)

        return emp


try:

    objEmployee = IO.input_employee_data()
except Exception as e:
    print(e)
print(objEmployee, type(objEmployee))
