from book import Books
from Students import Students




class Library:

    def __init__(self,books:Books=None):
        self.SHELF=books
        self.lend=[]

    def lend_book(self):
        ...