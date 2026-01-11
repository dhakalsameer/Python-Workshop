class Employee:
    def __init__(self,name,base_salary,):
        self.name = name
        self.base_salary = base_salary
    
    def calculate_salary(self):
        return self.base_salary

class Developer(Employee):
    def __init__(self,name,base_salary,overtime_hours):
        super().__init__(name, base_salary)
        self.overtime_hours = overtime_hours

    def calculate_salary(self):
        total = self.base_salary + self.overtime_hours * 500
        return total
    
class Manager(Employee):
    def __init__(self,name,base_salary,bonus,team_size):
        super().__init__(name, base_salary)
        self.bonus = bonus
        self.team_size = team_size
    
    def calculate_salary(self):
        total = self.base_salary + self.bonus + (self.team_size * 1000)
        return total

class salesPerson(Employee):
    def __init__(self,name, base_salary, commission_rate, sales_amount):
        super().__init__(name, base_salary)
        self.commission_rate = commission_rate
        self.sales_amount = sales_amount
    
    def calculate_salary(self):
        total = self.base_salary + (self.commission_rate * self.sales_amount)
        return total

def total_payroll(*employee):
    sum = 0
    for i in employee:
        sum = sum + i.calculate_salary()

    return sum


dev = Developer("Alice", 60000, overtime_hours=10) 
manager = Manager("Bob", 80000, bonus=10000, team_size=5) 


print(total_payroll(dev, manager))



        



