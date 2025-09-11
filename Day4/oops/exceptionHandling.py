def divison(n1,n2):
    try:
        res=n1/n2
    except ZeroDivisionError:
        print("Error:Division by zero is not allowed")
    else:
        print("result:",res)
divison(10,0)
divison(20,10)
    