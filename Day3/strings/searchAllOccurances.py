def searchAllOccurancesOfCharacter(s,char):
    new=[]
    for i in range(len(s)):
        if s[i]==char:
            new.append(i)
            return new
s="cvr college of engineering"
char=input("enter character:")
print("All occurances of character are at:",searchAllOccurancesOfCharacter(s,char))


