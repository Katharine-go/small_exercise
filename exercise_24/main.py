# 定义图书类，基本信息有书名title和作者author
# 借阅者borrower和待借阅者demanders
class Book(object):
    def __init__(self,title='', author=''):
        self.title = title
        self.author = author
    def info(self):
        return(self.title,self.author)
    def reader(self,borrower='',demanders=[]):
        self.borrower=borrower
        self.demanders=demanders

# 定义借阅者类，基本信息有姓名name,性别sex,身份证号ID
# 该借阅者借阅的书籍bookName(列表)
class Patron(object):
    def __init__(self,name='',sex='',ID='',borrowBooks=[]):
        self.name=name
        self.sex=sex
        self.ID=ID
        self.borrowBooks=borrowBooks
    def info(self):
        return(self.name,self.sex,self.ID,self.borrowBooks)
    #flag=1时，代表借书，flag=0时，代表还书
    def book(self,borrowBooks=[],title='',flag=1):
        #确保借阅者最多可借3本书
        if len(borrowBooks)<4  or flag==0:
            if flag==1:
                borrowBooks.append(title)
            else:
                borrowBooks.remove(title)
        else:
            print("最多可借阅三本图书！")
        return borrowBooks


class Library(object):
    """some operation on books and readers"""

    # some operation on books
    # add book
    def addBook(self, books=[], book=Book()):
        books.append(book.title)
        return books

    # delete book
    def deleteBook(self, books, book=Book()):
        books.remove(book.title)
        return books

    # find book,and return the index of the book
    def findBook(self, books, book=Book()):
        return books.index(book.title)

    # some operation on  readers
    # add reader
    def addReader(self, readers=[], patron=Patron()):
        readers.append(patron.name)
        return readers

    # delete reader
    def deleteReader(self, readers, patron=Patron()):
        readers.remove(patron.name)
        return readers

    # find reader,and return the index of the reader
    def findReader(self, readers, patron=Patron()):
        return readers.index(patron.name)

    # some operation on borrow and return book
    # borrow book
    def borrowBook(self, patron=Patron(), book=Book()):
        book.remove(book.title)
        patron.book(patron.borrowBooks, book.title, 1)
        return book, patron.borrowBooks

    # return book
    def returnBook(self, patron=Patron(), book=Book()):
        book.append(book.title)
        patron.book(patron.borrowBooks, book.title, 0)
        return book, patron.borrowBooks


# 测试
if __name__ == "__main__":
    library = Library()  # 创建Library类
    books = []  # 在图书馆的书
    readers = []  # 图书馆读者列表
    # 创建了4个Book类实例（4本书）
    book1 = Book("Gone with the Wind", "Margaret Mitchell")
    book2 = Book("Pride and Prejudice", "Jane Austen")
    book3 = Book("Oliver Twist", "Charles Dickens")
    book4 = Book("The Little Prince", "Antoine de Saint-Exupéry")
    # 创建了5个Patron类实例（5个借阅者）
    patron1 = Patron("Jack", "man", "121")
    patron2 = Patron("Bob", "man", "122")
    patron3 = Patron("Tim", "man", "123")
    patron4 = Patron("Ann", "woman", "124")
    patron5 = Patron("Jane", "woman", "125")

    # 图书的相关操作展示
    # 向books添加这些书
    library.addBook(books, book1)
    library.addBook(books, book2)
    library.addBook(books, book3)
    library.addBook(books, book4)
    # 此时，结果：['Gone with the Wind','Pride and Prejudice','Oliver Twist','The Little Prince']
    library.deleteBook(books, book3)
    # 此时，结果：['Gone with the Wind', 'Pride and Prejudice', 'The Little Prince']
    library.findBook(books, book2)
    # 此时，结果：1

    # 读者的相关操作展示
    # 向readers添加这些借阅者
    library.addReader(readers, patron1)
    library.addReader(readers, patron2)
    library.addReader(readers, patron3)
    library.addReader(readers, patron4)
    library.addReader(readers, patron5)
    # 此时，结果：['Jack', 'Bob', 'Tim', 'Ann', 'Jane']
    library.deleteReader(readers, patron2)
    # 此时，结果：['Jack', 'Tim', 'Ann', 'Jane']
    library.findReader(readers, patron4)
    # 此时，结果：2

    # 借阅图书和归还图书的操作
    # 借阅图书操作
    library.borrowBook(patron1, book1)
    library.borrowBook(patron1, book2)
    # 此时，结果：books= ['The Little Prince']
    # patron1.borrowBooks=['Gone with the Wind', 'Pride and Prejudice']
    # 验证一下，一个借阅者最多可借3本书
    library.addBook(books, book3)
    library.borrowBook(patron1, book3)
    # 当下面一句执行时，会打印最多可借3本书
    library.borrowBook(patron1, book4)

    # 归还图书操作
    library.returnBook(patron1, book1)
    # 此时，结果：books=['Gone with the Wind']
    # patron1.borrowBooks= ['Pride and Prejudice', 'Oliver Twist', 'The Little Prince']


