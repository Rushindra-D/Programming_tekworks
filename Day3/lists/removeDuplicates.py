def removeDuplicates(list):
    new=[]
    for i in list:
        if i not in new:
            new.append(i)
    print("List after removing duplicates:",new)
list=[1,2,3,4,5,1,2,3,4,1,2,3,1,2,1]
removeDuplicates(list)