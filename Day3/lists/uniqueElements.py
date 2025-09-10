def uniqueElements(list):
    new=[]
    for i in list:
        if i not in new:
            new.append(i)
    print("Unique elements are:",new)
list=[1,2,3,4,5,12,23,34,45,1,2,3,4,5]
uniqueElements(list)