# test_employee.py

from employee import Employee

def test_excellent_performance():
    emp = Employee("A", "1", "IT", 150000)  # Annual = 1800000
    assert emp.performance_category() == "Excellent"

def test_very_good_performance():
    emp = Employee("B", "2", "HR", 90000)  # Annual = 1080000
    assert emp.performance_category() == "Very Good"

def test_good_performance():
    emp = Employee("C", "3", "Finance", 60000)  # Annual = 720000
    assert emp.performance_category() == "Good"

def test_average_performance():
    emp = Employee("D", "4", "Admin", 40000)  # Annual = 480000
    assert emp.performance_category() == "Average"

def test_poor_performance():
    emp = Employee("E", "5", "Support", 20000)  # Annual = 240000
    assert emp.performance_category() == "Poor"
