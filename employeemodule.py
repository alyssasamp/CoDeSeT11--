class Employee:
    def __init__(self, name, emp_number):
        self.name= name 
        self.emp_number= emp_number 
        
    def set_name(self, name):
        self.name 
    
    def set_emp_number(self, emp_number):
        self.emp_number 
    
    def get_name(self):
        return self.name 
    
    def get_emp_number(self):
        return self.emp_number
    
    
class ProductionWorker(Employee):
    def __init__(self, name, emp_number, shift_number, hourly_pay_rate):
        super().__init__(name, emp_number)
        self.shift_number= shift_number
        self.hourly_pay_rate= hourly_pay_rate
        
        def set_shift_number(self, shift_number):
            self.shift_number= shift_number
            
            
        def set_hourly_pay_rate(self, hourly_pay_rate):
            self.hourly_pay_rate= hourly_pay_rate
            
            
        def get_shift_number(self):
            return self.shift_number
        
        def get_hourly_pay_rate(self):
            return self.hourly_pay_rate
        
           