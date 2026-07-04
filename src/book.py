
class Book:

    def __init__(self,name:str=None,author=None,year:int=None,ID:int=None,**Hashmap):
        self.name=name
        self.author=author
        self.year=year
        self.Book_ID=ID

        if Hashmap:
            for key , value in Hashmap.items():
                self.key=value







class Books:

    """
        this class is for books the main attr is arr of books 
        
    """
    def __init__(self,books:list[Book]=None)->None:

        self.books=books if books is not None else []

    def __len__(self)->int:
        return len(self.books)
    
    
    def __getitem__(self, key)-> str:
        return self.books[key]


    def add_book(self,new_book:Book)->None:
        """
        this function is used to add new books for library
        """
        self.books.append(new_book)
        





