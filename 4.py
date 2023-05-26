class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def calculate_bonus():
        pass

class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
        
    def calculate_bonus(self):
        return self.salary+((self.salary*25)/100)
    
class Developer(Employee):
    def calculate_bonus(self):
        return self.salary+((self.salary*15)/100)
    
m = Manager('Иван', 35000)
d = Developer('Петр', 20000)

print(m.calculate_bonus())
print(d.calculate_bonus())