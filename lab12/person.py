from mammal import Mammal

class Person(Mammal):
    def __init__(self, name, age, height):
        super().__init__(age)
        self.name = name
        self.height = height

    # Overriding mammal's speak method
    def speak(self):
        print("Hello!")

    # Overriding mammal's __str__ method
    def __str__(self):
        return f"This person's name is {self.name}. Their heart is beating at {self.heart}bpm."
