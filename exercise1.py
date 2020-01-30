class Human:
    name = ""
    age = None
    sex = ""

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


