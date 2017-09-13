class Dog:
    kind = "canie"

    def __init__(self, name):
        self.name = name
        self.tricks = []
        self.age = 0

    def add_trick(self, trick):
        self.tricks.append(trick)


d = Dog('Fido')
e = Dog('Buddy')
print(d.kind)
print(e.kind)
print(d.name)
print(e.name)
d.add_trick("aaa")
e.add_trick('eee')
print(d.tricks)
print(d.age)


