def countOccurancesCharacter(s):
    dict={}
    for i in s:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    s=""
    for char in dict.keys():
        s+=char
        s+=str(dict[char])
    print(s)


s="aaabbca"
countOccurancesCharacter(s)


        