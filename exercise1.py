class Human:
    name = ""
    age = None
    sex = ""

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

citizen1 = Human()
citizen1.name = "Mike"
citizen1.age = 23
citizen1.sex = "male"

print(f"Object - {citizen1.sex}, {citizen1.name}, age: {citizen1.age}")
citizen1.say_hello()
citizen1.move()
citizen1.think()
