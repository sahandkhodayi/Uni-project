from book import Books,Book
from Students import Students,Student


_INFO={

    "title": lambda b: b.name,
    "author": lambda b: b.author,
    "ID": lambda b: b.Book_ID,
}




class Library:

    def __init__(self,books:Books=None,Students:Students=None):
        self.SHELF=books if len(books) else []
        self.students=Students if len(Students) else []
        self.lend=[]
        self.All_Books=books if len(books) else []

    def lend_book(self,Student:Student,book:Book)->None:
        if book not in self.SHELF.books:
            raise ValueError("book is not available!")
        
        if book.borrowed :
            raise ValueError("book already taken!")
        
        
        if Student not in self.students.Students:
            raise ValueError("student couldnt found!")

        Student.lend_books.append(book)
        book.borrowed=True

        self.lend.append(book)
        
        self.SHELF.remove(book)
        return
    

            
    def search(self,Key:str,Intel:str)->Book:

        func=_INFO[Key]
        for Bk in self.SHELF.books:
            if func(Bk).lower()==Intel.lower:
                return Bk
            
        return None    
    
    def Return_book(self,student:Student,book:Book)->None:
        if book not in self.lend:
            raise ValueError("book is not in lend")
        if not book.borrowed:
            raise ValueError("BOOK already available!")
        
        if book not in self.All_Books:
            raise ValueError("book doesnt belong in this library!")
        
        if student not in self.students.Students:
            raise ValueError(" Student iis not in our database!")
        

        student.lend_books.remove(book)
        book.borrowed=False
        self.SHELF.append(book)
        self.lend.remove(book)
        return None
    
    def available_books(self)->list[Book]:
        return self.SHELF
    
    def borrowed_books(self)->list[Book]:

        return self.borrowed_books
    









