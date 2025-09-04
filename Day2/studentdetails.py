student_name=input("Enter name of the student")
student_no=int(input("Enter stiudent number"))
m1=int(input("enter marks in  maths"))
m2=int(input("Enter marks in physics"))
m3=int(input("Enter marks in chemistry"))
print(student_name)
print(student_no)
avg=(m1+m2+m3)/3
print(avg)
if avg>80:
    print("Distension")
elif avg>70 and avg<=80:
    print("A grade")
elif avg>51 and avg<=70:
    print("B grade")
elif avg>=40:
    print("pass")
else:
    print("Fail")
    