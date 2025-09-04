def prime(n):
    f=2
    while(f<=n):
        if(n%f==0):
            return False
        f+=1
    return True
n=(int)(input("Entyer n:"))
print(prime(n))