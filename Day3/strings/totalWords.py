def totalWordsCounts(s):
    count=1
    for i in s:
        if i==' ':
            count=count+1
    return count    
s="Cvr college of engineering"
print("Total words in s are:",totalWordsCounts(s))