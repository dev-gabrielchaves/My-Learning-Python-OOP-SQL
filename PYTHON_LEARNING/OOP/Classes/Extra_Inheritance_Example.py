class Employee:

    raise_amount = 1.05

    def __init__(self, first, last, pay) -> None:
        self.first = first
        self.last = last
        self.pay = pay
    
    def full_name(self) -> str:
        return self.first + ' ' + self.last
    
    def apply_raise(self) -> None:
        self.pay = self.pay * self.raise_amount

class Developer(Employee):
    
    raise_amount = 1.10 #Changing the variable 'raise_amount' specifically to the class 'Developer'
    
    def __init__(self, first, last, pay, prog_lang) -> None:
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang #Adding the attribute 'prog_lang' exclusively to the class 'Developer'.

class Manager(Employee):

    def __init__(self, first, last, pay, employees = None) -> None: #When setting 'employees = None' that means that if no parameter is added to the object of the class 'Manager', by default it will be = None.
        super().__init__(first, last, pay)
        
        if employees == None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, employee):
        self.employees.append(employee)
    
    def remove_employee(self, employee):
        self.employees.remove(employee)
    
    def list_of_employees(self):

        for employee in self.employees:
            print('---> ', employee.full_name())

dev_1 = Developer('Gabriel', 'Chaves', 50000, 'PYTHON')
dev_2 = Developer('João', 'Camboim', 40000, 'Ruby')

mngr_1 = Manager('Roberto', 'Camboim', 90000, [dev_1])

mngr_1.list_of_employees()
mngr_1.add_employee(dev_2)

mngr_1.list_of_employees()