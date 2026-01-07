# employee.py

class Employee:
    def __init__(self, name, emp_id, department, monthly_salary):
        self.name = name
        self.emp_id = emp_id
        self.department = department
        self.monthly_salary = monthly_salary

    def annual_salary(self):
        return self.monthly_salary * 12

    def performance_category(self):
        annual = self.annual_salary()
        if annual >= 1200000:
            return "Excellent"
        elif annual >= 800000:
            return "Very Good"
        elif annual >= 500000:
            return "Good"
        elif annual >= 300000:
            return "Average"
        else:
            return "Poor"


# For running manually (optional)
if __name__ == "__main__":
    emp = Employee("Akash", "101", "IT", 50000)  # Example values
    print(f"Name: {emp.name}")
    print(f"Annual Salary: {emp.annual_salary()}")
    print(f"Performance: {emp.performance_category()}")
