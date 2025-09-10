def highestFrequencyCharacter(s):
    d={}
    for i in s:
        if i in d:
            d[i]=d[i]+1
        else:
            d[i]=1
    max=0
    char=''
    for i in d:
        if d[i]>max:
            max=d[i]
            char=i
    print(char,max)
    return char,max
s="aaabbca"
char,max=highestFrequencyCharacter(s)