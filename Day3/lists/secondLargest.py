def secondLargestElement(list):
        for i in range(len(list)):
                for j in range(i+1,len(list)):
                        if list[i]>list[j]:
                                list[i],list[j]=list[j],list[i]
        print("Second largest element is:",list[-2])


list=[2,10,9,5,17,20,15]
secondLargestElement(list)