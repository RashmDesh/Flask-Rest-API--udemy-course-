class Book:
    Types=("hardcover","paperback")

    def __init__(self,name,book_type,weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight


    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighting {self.weight}g>"
    
    @classmethod
    def hardcover(cls, name , page_weight):
        return Book(name ,Book.Types[0],page_weight+100)

    @classmethod
    def paperback(cls, name , page_weight):
        return cls(name ,cls.Types[1],page_weight+100)

book =Book.hardcover("Harry potter",1500)

light=Book.paperback("python 101",600)
print(book)
print(light)
