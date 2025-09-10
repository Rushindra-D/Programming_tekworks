def totalNumberOfAlphabets(s):
    c=0
    for i in s:
        if (i>='a' and i<='z') or (i>='A' and i<='Z'):
            c+=1
    print("Total number of alphabets in the string is:",c)
def totalNumberOfDigits(s):
    c=0
    for i in s:
        if i>='0' and i<='9':
            c+=1
    print("Total number of digits in the string is:",c)
def totalSpecialCharcacters(s):
    c=0
    for i in s:
         if not((i>='a' and i<='z') or (i>='A' and i<='Z') or (i>='0' and i<='9')):
            c+=1
    print("Total number of special characters in the string is:",c)
s="Rushindra@123"
totalNumberOfAlphabets(s)
totalNumberOfDigits(s)
totalSpecialCharcacters(s)