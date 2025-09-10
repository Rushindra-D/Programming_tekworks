def stringLength(s):
    c=0
    for i in s:
        c+=1
    return c

def compareStrings(s1,s2):
    if s1==s2:
        print("Strings are equal")  
    elif s1>s2:
        print("first string has more characters")
    else:
        print("second string has more characters")
def concatenateStrings(s1,s2):
    return s1+s2
print(stringLength("Rushindra"))
compareStrings("Rushindra","Vishnu")
print(concatenateStrings("Rushindra","Vishnu"))

    