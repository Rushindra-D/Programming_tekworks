def duplicatesCount(list):
    c=0
    new=[]
    for i in list:
        if i not in new:
            new.append(i)
        else:
            c+=1
    print("Number of duplicate elements are:",c)
list=[1,2,3,4,5,1,2,3,4,1,2,3,1,2,1]
duplicatesCount(list)