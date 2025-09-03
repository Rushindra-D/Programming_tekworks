def checkdivisibility(n):
    if n%5==0 and n%11==0:
        return "divisible by 5 and 11"
    else:
        return "false"
checkdivisibility(55)