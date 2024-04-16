class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return str({'title':self.title, 'author':self.author})
    
    def __len__(self):
        return self.pages
    
    def __del__(self):
        print(self.title + " is deleted from memory")

book = Book("Python Rocks", "Han", 210)
print(book)
print(len(book))
del book
#print(book)

