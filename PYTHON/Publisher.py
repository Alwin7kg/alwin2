class Publisher:
    def __init__(self,n):
        self.name=n
class Book(Publisher):
    def __init__(self,name,title,author):
        Publisher.__init__(self,name)
        self.title=title
        self.author=author
    def display(self):
        print("Title:\t",self.title)
        print("Author:\t",self.author)
        print("Name:\t",self.name)
class Python(Book):
    def __init__(self,name,title,author,no_of_pages,price):
        Book.__init__(self,name,title,author)
        self.no_of_pages=no_of_pages
        self.price=price
    def display(self):
        print("Publisher name:\t",self.name)
        print("Title:\t\t",self.title)
        print("Author:\t\t",self.author)
        print("Number of pages: ",self.no_of_pages,"pages")
        print("Price:\t\t Rs:",self.price)

#ain
p=Python("Penguin Publishers","When I am With You","Durjoy Dutta",320,149)
p.display()
