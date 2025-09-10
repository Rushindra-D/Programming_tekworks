def setExample(s):
    print("Set is:",s)
    s.add(11)
    print("Set after adding 11 is:",s)
    s.remove(5)
    print("Set after removing 5 is:",s)
    s.pop()
    print("Set after pop is:",s)

s={1,2,3,4,5,6,7,8,9,10}
setExample(s)
