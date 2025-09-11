class Employee:
    def __init__(self,name, salary):
        self.name = name
        self.salary= salary
        
    def display(self):
        print("Name:",self.name)
        print("Salary:",self.salary)
class Manager(Employee):
    def __init__(self, name, salary,department):
        super().__init__(name, salary)
        self.department=department
    def display(self):
        print("Name:",self.name)
        print("Salary:",self.salary)
        print("Department:",self.department)
e1=Employee("Rishi",90000)
e1.display()
m1=Manager("santhosh",90000,"cse")
m1.display()











