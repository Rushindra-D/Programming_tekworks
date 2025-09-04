def sum_of_digits(n):
   s=0
   while(n>0):
      s+=n%10
      n//=10
   return s
n=(int)(input("enter vaue of n:"))
print(sum_of_digits(n))

    