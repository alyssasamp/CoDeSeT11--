class Employee:
    def __init__(self, name, employee_id):
    self.name= name
    self.employee_id= employee_id
    
    def display_info(self):
        print("Name: {self.name}")
        print("Employee ID: {self.employee_id}")
        
        
class ShiftSupervisor(Employee):
    def __init__(self, name, employee_id, annual_salary, annual_production_bonus):
        super().__init__(name, employee_id)
        self.annual_salary= annual_salary
        self.annual_production_bonus= annual_production_bonus 
        
    def display_info(self):
        super().display_info()
        print("Annual Salary: ${self.annual_salary}")
        print("Annual Production Bonus: ${self.annual_production_bonus}")
            
    def calculate_total_income(self):
        return self.annual_salary + self.annual_production_bonus 
       