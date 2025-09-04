def pattern(r,c):
    for i in range(1,r+1):
        for j in range(1,c+1):
            if i==j or i+j==r+1 :
               print("$",end=" ")
            else:
                print("*",end=" ")
        print()
print(pattern(5,5))
