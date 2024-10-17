import model as sql

class Book :
    '''
    my book class
    '''
    library_name = "Tehran Library"
    total_books = 0
    def __init__(self, isbn , title, author , year, price, pages, genre) :
        print(f"Initializing Book with ISBN: {isbn}")
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.price = price
        self.pages = pages
        self.genre = genre
        Book.total_books+=1
        sql.insert_book(self.isbn, self.title, self.author, self.year, self.price, self.pages, self.genre)

    @property
    def isbn(self):
        return self._isbn
    @isbn.setter
    def isbn(self,value):
        if 10000000 <= value <= 99999999 :
            self._isbn = value
        else :
            raise ValueError("isbn of the book must be an 8 digit number")
        
    @property
    def price(self):
        return self._p
    @price.setter
    def price(self,value):
        if 20000 <= value <= 1000000 :
            self._p = value
        else :
            raise ValueError("Price of the book must be between 200K and 1M")
        
    @staticmethod
    def allbooks():
        return sql.allbooks()
    
    @staticmethod
    def delete_book(isbn):
        return sql.delete_book(isbn)
    
    @staticmethod
    def update_book(isbn1,isbn2):
        return sql.update_book(isbn1,isbn2)
    
    @staticmethod
    def update_book1(price,isbn):
        return sql.update_book1(price,isbn)


