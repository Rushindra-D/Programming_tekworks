def vowelsAndConsonantsCount(s):
    v=0
    c=0
    for i in s:
        if (i>='a' and i<='z') or (i>='A' and i<='Z'):
            if i in 'aeiouAEIOU':
                v+=1
            else:
                c+=1
    print("Number of vowels:",v)
    print("Number of consonants:",c)
s="Rushindra"
vowelsAndConsonantsCount(s)