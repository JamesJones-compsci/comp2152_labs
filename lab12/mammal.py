from heart import Heart
# import heart

class Mammal:
    def __init__(self, age):
        self.age = age
        self.heart = Heart()  # Create an instance of heart

    def speak(self):
        print("Grr...")

    def __str__(self):
        return f"Mammal is {self.age} years old"
