customer_name=input("enter name of the customer")

pmr=int(input("Enter present month reading"))
lmr=int(input("Enter last month reading"))
tu=pmr-lmr
cb=0
if  tu<=50:
    cb=tu*3.80
elif tu<=100:
    cb=(50*3.80)+(tu-50)*4.20
elif tu<=200:
    cb=(50*3.80)+(50*4.20)+(tu-100)*5.10
elif tu<=300:
    cb=(50*3.80)+(50*4.20)+(100*5.10)+(tu-200)*6.30
else:
    cb=(50*3.80)+(50*4.20)+(100*5.10)+(200*6.30)+(tu-300)*7.5

print(cb)
