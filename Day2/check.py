def check(c):
    if c>='a' and c<="z" or c>="A" and c<="Z":
        print("it is an alphabet")

    elif c>='0' and c<='9':
        print("it is digit")
    else:
        print("it is an special character")
check("r")
