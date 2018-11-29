#
#
#

# function


def f(x):
    return (x+1)

y = f(1)


print(y)


def teach_medical_students(class_size):
    print("hello class", class_size, "students! Wow!")


teach_medical_students(40)


class Shark:

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def hello(self):
        print("Hello I'm a shark! My name is", self.name)

    def endangered(self):
        if self.type == "Hammerhead":
            print("Help! I am endangered")
        else:
            print("I am not endangered")


a = Shark("Frank", "Hammerhead")
b = Shark("Bob", "Great White")

b.endangered()
