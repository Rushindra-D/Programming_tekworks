def addBook(book,id,title):
    book[id]=""
    book[id]=title
    print("Book added ")
    return book
def removeBook(book,id):
    if id in book.keys():
        del book[id]
        print("Book removed")
    else:
        print("book not found")
def searchBook(book,id):
    if id in book.keys():
        print("Book found")
    else:
        print("Book not found")
def updateTitle(book,id):
    if id in book.keys():
        title=input("Enter new title:")
        book[id]=title
        print("Title updated")
    else:
        print("Book not found")

def displayBooks(book):
    for i in book.keys():
        print(i,":",book[i])
def totalBooks(book):
    print("Total books in library:",len(book))
def titleExists(book,title):
    if title in book.values():
        print("Title exists")
    else:
        print("not exits")
book={}
n=int(input("Enter number of books to be added:"))
for i in range(n):
    id=int(input("Enter book id:"))
    title=input("Enter book title:")
    addBook(book,id,title)
removeBook(book,2)
searchBook(book,1)
updateTitle(book,2)      
displayBooks(book)
totalBooks(book)
titleExists(book,"Python")

