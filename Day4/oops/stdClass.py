class Student:
    def __init__(self,name, rollno, marks):
        self.name = name
        self.rolln0 = rollno
        self.marks=marks
    def display(self):
        print("Name:",self.name)
        print("Roll No:",self.rolln0)
        print("Marks:",self.marks)
s1=Student("Rishi",101,95)
s2=Student("Santhosh",102,9)
s1.display()
s2.display()