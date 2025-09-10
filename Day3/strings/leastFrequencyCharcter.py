def leastFrequencyCharacter(s):
    d={}
    for i in s:
        if i in d:
            d[i]=d[i]+1
        else:
            d[i]=1
    min=1000
    char=''
    for i in d:
        if d[i]<min:
            min=d[i]
            char=i
    print(char,min)
    return char,min
s="aaabbca"
char,min=leastFrequencyCharacter(s)