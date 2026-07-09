from book import Book







class Student:

    def __init__(self,books:list[Book],name:str=None,Student_ID:int=None,Phone_number:int=None,**Hashmap)->None:

        self.name=name
        self.Student_ID=Student_ID
        self.Phone_number=Phone_number
        self.lend_books= books if len(books)!=0 else []

        if Hashmap:
            for key , value in Hashmap.items():
                self.key=value



class Students:
    """
    this class is mainly for stududents or member info of the library 
    attrb will be writen for this class soon !
    """

    def __init__(self,Students:list[Student]=None):
        self.Students=Students if Students  else []

    def __len__(self)->int:
        return len(self.Students)    
    
    def __getitem__(self, key:int)->Student:
        return self.Students[key]

    def add_student(self,student:Student)->None:

        self.Students.append(student)    

