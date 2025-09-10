def evenandoddCount(list):
    evencount=0
    oddcount=0
    for i in list:
        if i%2==0:
            evencount+=1
        else:
            oddcount+=1
    print("Even count is:",evencount)
    print("odd count is:",oddcount)
list=[1,2,3,4,5,6,7,8,9,10]
evenandoddCount(list)