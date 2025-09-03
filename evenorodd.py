#to check given number even or odd 
def evenorodd(n):
    if n%2==0:
        print("number is even")
    else:
        print("odd number")
evenorodd(6)
def evencheck(n):
    if n<0:
        return -1
    return n%2==0
print(evencheck(15))