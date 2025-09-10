def frequencyCount(list):
    d={}
    for i in list:
        if i in d:
            d[i]=d[i]+1
        else:
            d[i]=1
    print("Frequency count is:",d)
list=[1,2,3,4,5,1,2,3,4,1,2,3,1,2,1]
frequencyCount(list)