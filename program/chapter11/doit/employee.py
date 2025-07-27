class Employee:
    def __init__(self, sex, salary):
        self.sex = sex
        self.salary = salary
    
    def give_raise(self, raise_num = 500_000):
        self.salary += raise_num