import logging
from collections import defaultdict

# Налаштування логування
logging.basicConfig(filename='vet_clinic.log', level=logging.INFO, format='%(asctime)s - %(message)s')

class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"Name: {self.name}, Position: {self.position}, Salary: {self.salary}"


class VeterinaryClinic:
    def __init__(self):
        self.employees = []
        self.command_usage = defaultdict(int)
        self._initialize_employees()

    def _initialize_employees(self):
        initial_employees = [
            ("Маша Елизавета", "Ветеринар", 50000),
            ("Коля Чейпеш", "Асистент ветеринара", 30000),
            ("Михайло Рашов", "Хірург", 70000),
            ("Катерина Шевченко", "Адміністратор", 40000),
            ("Азербаджан Альтерєнко", "Лаборант", 35000),
            ("Маріання Володимерівна", "Зоотехнік", 45000)
        ]
        for name, position, salary in initial_employees:
            self.add_employee(name, position, salary)

    def add_employee(self, name, position, salary):
        new_employee = Employee(name, position, salary)
        self.employees.append(new_employee)
        logging.info(f"Added employee: {name}, Position: {position}, Salary: {salary}")
        print(f"Employee {name} added.")

    def remove_employee(self, name):
        for employee in self.employees:
            if employee.name == name:
                self.employees.remove(employee)
                logging.info(f"Removed employee: {name}")
                print(f"Employee {name} removed.")
                return
        logging.warning(f"Attempted to remove non-existent employee: {name}")
        print(f"Employee {name} not found.")

    def view_employees(self):
        if not self.employees:
            print("No employees in the clinic.")
        else:
            for employee in self.employees:
                print(employee)
        logging.info("Viewed employee list")

    def update_salary(self, name, new_salary):
        for employee in self.employees:
            if employee.name == name:
                employee.salary = new_salary
                logging.info(f"Updated salary for {name} to {new_salary}")
                print(f"Salary for {name} updated to {new_salary}.")
                return
        logging.warning(f"Attempted to update salary for non-existent employee: {name}")
        print(f"Employee {name} not found.")

    def update_position(self, name, new_position):
        for employee in self.employees:
            if employee.name == name:
                employee.position = new_position
                logging.info(f"Updated position for {name} to {new_position}")
                print(f"Position for {name} updated to {new_position}.")
                return
        logging.warning(f"Attempted to update position for non-existent employee: {name}")
        print(f"Employee {name} not found.")

    def command_frequency(self):
        print("\nCommand usage frequency:")
        for command, count in self.command_usage.items():
            print(f"{command}: {count} times")


def main():
    clinic = VeterinaryClinic()
    
    commands = {
        '1': ('Add Employee', lambda: clinic.add_employee(
            input("Enter name: "), 
            input("Enter position: "), 
            float(input("Enter salary: "))
        )),
        '2': ('Remove Employee', lambda: clinic.remove_employee(input("Enter name of the employee to remove: "))),
        '3': ('View Employees', clinic.view_employees),
        '4': ('Update Employee Salary', lambda: clinic.update_salary(
            input("Enter name of the employee: "), 
            float(input("Enter new salary: "))
        )),
        '5': ('Update Employee Position', lambda: clinic.update_position(
            input("Enter name of the employee: "), 
            input("Enter new position: ")
        )),
        '6': ('Command Frequency', clinic.command_frequency),
        '7': ('Exit', lambda: print("Exiting..."))
    }

    while True:
        print("\nCommands:")
        for key, (description, _) in commands.items():
            print(f"{key}. {description}")

        choice = input("Enter your choice: ")

        if choice in commands:
            description, action = commands[choice]
            clinic.command_usage[description] += 1
            action()
            if choice == '7':
                break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
