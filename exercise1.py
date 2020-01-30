class Human:

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def say_hello(self):
        print("Hi! My name is " + self.name)
    
    def move(self):
        if self.sex == "male":
            print("*he moves*")
        else:
            print("*she moves*")

    def think(self):
        if self.age > 2:
            print("Ok! I will think about it!")
        else:
            print("Huh?")

citizen1 = Human("Mike", 23, "male")


print(f"\n Object - {citizen1.sex}, {citizen1.name}, age: {citizen1.age}\n")
citizen1.say_hello()
citizen1.move()
citizen1.think()

class Book:
 
    def __init__(self, title, pages, author, year, owner):
        self.title = title
        self.pages = pages
        self.author = author
        self.year = year
        self.owner = owner
    
    def info(self):
        print(f"Title: {self.title}, \n author: {self.author}, \n year of publication: {self.year}, \n number of pages: {self.pages}, \n owner: {self.owner} ")

    def new_owner(self, new_owner):
        self.owner = new_owner
    
book1 = Book("A Fest for Crows", 753, "George R. R. Martin", 2005, "Martin")
book2 = Book("The Forever War", 236, "Joe Haldeman", 1974, "Martin")
book3 = Book("The Lady of the Lake", 544, "Andrzej Sapkowski", 1999, "Martin")
    
my_library = [book1, book2, book3]

for i in my_library:
    print(i.info())


        

