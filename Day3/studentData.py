list=[]
def studentData(rollno,name,marks):
    
    list.append((rollno,name,marks))
def display(list):
    for i in list:
        print(i)
def highestMarksStudent(list):
    h=0
    for i in list:
        if i[2]>h:
            h=i[2]
            name=i[1]
    print("Student with highest marks is:",name,"with marks",h)
def minimun75marks(list):
    for i in list:
        if i[2]>75:
            print(i[1],"has scored more than 75 marks")
studentData(101,"Rushindra",95)
studentData(102,"Amit",85)  
studentData(103,"Suresh",75)    
studentData(104,"Ramesh",65)
studentData(105,"Mahesh",55)
display(list)
highestMarksStudent(list)
minimun75marks(list)



