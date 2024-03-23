
class books:
    
    def __init__(self, title, year, author):
        self.title = title
        self.year = year
        self.author = author
        
        
    def info(self):
        print(self.title + " " + str(self.year) + " " + self.author)
        

book1 = books('Home before dark ', 2020,'Riley Sager')


book1.info()


# example 2


class Book2:
    
    def __init__(self, title, year, author):
        self.title = title
        self.year = year
        self.author = author
        
    def info(self):
        print(self.title + " " + str(self.year) + " " + self.author)
        
book2 = Book2('Tokio Blues', 1987,'Haruki Murakami')

book2.info()

# ejemplo 3


class Libro:
    
    def __init__(self, title, year, author):
        self.title = title
        self.year = year
        self.author = author
        self.info = f'Book title: {title}, published date: {year} and author: {author}'
        
    def infomation(self):
        print('The book information is: ', self.info)
        
        
        
    
        
book3 = Libro('The shinning', 1977,'Stephen King')

book3.infomation()
print(book3.title)
print(book3.author)
print(book3.info)






