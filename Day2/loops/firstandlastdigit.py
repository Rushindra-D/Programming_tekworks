def firstAndLastDigit(n):
    l=n%10
    f=0
    while(n>0):
        f=n%10
        n//=10
    return f,l
print(firstAndLastDigit(123))