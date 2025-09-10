def deleteElement(list,position):
    if position<0 or position>=len(list):
        print("Invalid")
    new=[]
    for i in range(len(list)):
        if i!=position:
            new.append(list[i])
    print("New list is:",new)
list=[10,20,30,40,50,60]
position=int(input("Enter the position"))
deleteElement(list,position)