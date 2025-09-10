def removeDuplicates(l1,l2,l3):
    s1=set(l1)
    s2=set(l2)
    s3=set(l3)  
    l1=list(s1)
    l2=list(s2)
    l3=list(s3)
    return s1,s2,s3
def totalNumberOFUniqueAttendees(l1,l2,l3):
    s1,s2,s3=removeDuplicates(l1,l2,l3)
    total=len(s1.union(s2).union(s3))
    print("Total number of unique attendees in three days:",total)
    return total
    
def allThreeDaysAttendees(l1,l2,l3):
    s1,s2,s3=removeDuplicates(l1,l2,l3)
    c=(s1.intersection(s2)).intersection(s3)
    print("Attendees present in all three days:",c)
    return c
def oneDayAttendees(l1,l2,l3):
    s1,s2,s3=removeDuplicates(l1,l2,l3)
    One=(s1.symmetric_difference(s2)).symmetric_difference(s3)
    print("Attendees present in only one day:",One)
    return One
def pairwiseOverlapCount(l1,l2,l3):
    s1,s2,s3=removeDuplicates(l1,l2,l3)
    pairwiseOverlap1=(s1.intersection(s2))
    pairwiseOverlap2=(s2.intersection(s3))
    pairwiseOverlap3=(s3.intersection(s1))
    print("Attendees present in day1 and day2:",len(pairwiseOverlap1))
    print("Attendees present in day2 and day3:",len(pairwiseOverlap2)) 
    print("Attendees present in day3 and day1:",len(pairwiseOverlap3))
    return pairwiseOverlap1,pairwiseOverlap2,pairwiseOverlap3


l1=['abc@gmail.com','def@gmail.com','ghi@gmail.com']
l2=['def@gmail.com','ghi@gmail.com','klm@gmail.com']
l3=['ghi@gmail.com','klm@gmail.com','npo@gmail.com']
removeDuplicates(l1,l2,l3)
totalNumberOFUniqueAttendees(l1,l2,l3)
allThreeDaysAttendees(l1,l2,l3)
oneDayAttendees(l1,l2,l3)
pairwiseOverlapCount(l1,l2,l3)





