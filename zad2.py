from zad1 import Student

class Library:
    def __init__(self, city:str, street:str, zip_code:str, open_hours:str, phone:int):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self) -> str:
        return f'Biblioteka w {self.city} na ulicy {self.street} o kodzie pocztowym {self.zip_code} otwarta w godzinach {self.open_hours}, nr telefonu: {self.phone}'
        


class Employee:
    def __init__(self, first_name:str, last_name:str, hire_date:str, birth_date:str, city:str, street:str, zip_code:str, phone:str):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self) -> str:
        return f'Pracownik {self.first_name} {self.last_name} zatrudniony {self.hire_date}, mieszkający w mieście: {self.city} {self.zip_code}, numer kontaktowy: {self.phone} '
    

class Book:
    def __init__(self, library:str, publication_date:str, author_name:str, author_surname:str, number_of_pages:int):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages
    def __str__(self) -> str:
        return f'Kaiążka wydana w {self.publication_date}, napisana przez {self.author_name} {self.author_surname}, liczy {self.number_of_pages} stron, dostępna w bilbliotece: {self.library}'

class Order:

    def __init__(self, employee: Employee, student: Student, books: Book, order_date:str):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self) -> str:
        return f'Książka wypożyczona przez {self.student.name} w dniu {self.order_date}, przekazana przez {self.employee.first_name} {self.employee.last_name}'
    


    
Library_1 = Library('Katowice','Główna 12', '40-007', '8-19',890765342)
Library_2 = Library('Rybnik','Kwiatowa 54', '40-002', '7-16',456675324)

book_1 = Book('Biblioteka Rybnik', '12-10-1999', 'Stephen', 'King', 468)
book_2 = Book('Biblioteka Katowice', '12-10-2020', 'Adam', 'King', 920)
book_3 = Book('Biblioteka Katowice', '21-08-2008', 'John', 'King', 789)
book_4 = Book('Biblioteka Chorzów', '04-10-2004', 'Peter', 'King', 908)
book_5 = Book('Biblioteka Rybnik', '03-12-1994', 'Jason', 'King', 605)

employee_1 = Employee('Jan','Kowalski','12-12-2019','10-07-1992','Rybnik', 'Prosta 11', '44-200', 502678543)
employee_2 = Employee('Adam','Nowak','12-12-2019','09-11-1986','Katowice', 'Warszawska 43/4', '44-007', 506786456)
employee_3 = Employee('Jan','Kowalski','12-12-2019','23-02-1998','Gliwice', 'Główna 22', '44-009', 806789465)

student_1 = Student('Kamil Kowal',66)
student_2 = Student('Piotr Nowakowski',22)


order_1 = Order(employee_1, student_1, book_1, '20-11-2021' )
order_2 = Order(employee_2, student_2, book_2, '05-11-2020' )
print(order_1)
print(order_2)