from datetime import datetime


"""
System for logging company's employees
Company is divided into departments, no more than 20 employees per department
Each department has a name, abbreviation and manager
Each employee has a id number, surname and forename, patronymic, passport data, date and place of birth, address of residency
For each full year an employee works their salary increases 1.2%
employees can change positions and the system must remember history of employee's previous positions
employees have vacations each year, length of which depends position is measured in days per calendar year of work
system must store data on all employee vacations
no more than 5 employees can be on vacation at the same time from each department
"""

#classes for departments
class Department:
    def __init__(self, salary, name, abbreviation, manager):
        self.base_salary = salary
        self.name = name
        self.abbreviation = abbreviation
        self.manager = manager
        self.employees = []
    
    # add employee to department
    def add_employee(self, employee):
        if len(self.employees) < 20:
            self.employees.append(employee)
            return True
        return False    

    # remove employee from department
    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)
            return True
        return False

#classes for possible employee positions
class Position:
    def __init__(self, name, salary, vacation):
        self.name = name
        self.salary = salary
        self.vacation = vacation

#employee class
class Employee:
    def __init__(self, name, surname, idn, patronymic, passport, dob, pob, address, position):
        self.name = name
        self.surname = surname
        self.id = idn
        self.patronymic = patronymic
        self.passport = passport
        self.dob = dob
        self.pob = pob
        self.address = address
        self.position = position
        self.vacations = []
        self.last_increase = datetime.now()
    
    def change_position(self, position):
        self.position = position
    
    def request_vacation(self, length, details):
        if len(self.position.vacation) <= length:
            self.position.vacation -= length
            self.vacations.append(details)
            return True
        return False
    
    def salary_increase(self):
        if datetime.now().year - self.last_increase.year > 0:
            self.last_increase = datetime.now()
            self.position.salary *= 1.2
            return True
        return False

        
