def addItem(c,item):
    c.append(item)
def removeItem(c,item):
    if item in c:
        c.remove(item)
    else:
        print("Invalid")
def searchItem(c,item):
    if item in c:
        print("Found")
    else:
        print("not found")
def displayItems(c):
    print("Cart items are:",c) 
def totalItems(c):
    print("Total items in cart:",len(c))
def sortItems(c):
    c.sort()
def clearCart(c):
    c.clear()


c=[]
n=int(input("Enter number of items to be added:"))
while True:
    print("1.Add item\n2.Remove item\n3.Search item\n4.Display items\n5.Total items\n6.sort items\n7.Clear Cart\n8.Exit")
    ch=int(input("Enter choice:"))
    if ch==1:
        item=input("Enter item to be added:")
        addItem(c,item)
    elif ch==2:
        item=input("Enter item to be removed:")
        removeItem(c,item)
    elif ch==3:
        item=input("Enter item to be searched:")
        searchItem(c,item)
    elif ch==4:
        displayItems(c)
    elif ch==5:
        totalItems(c)  
    elif ch==6:
        sortItems(c)
        print("Items sorted")
    elif ch==7:
        clearCart(c)
        print("Cart cleared")
    else:
        break



