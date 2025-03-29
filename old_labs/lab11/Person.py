class Person:
    def __init__(self, name, age, height):
        self.__name = name
        self.__age = age
        self.__height = height
        self.public_prop = "I'm public"

        print("Constructing the Person object")

    def __del__(self):
        print("The garbage collector is automatically destroying the Person object")

    # Basic getter/setter
    # def get_name(self):
    #    return self.__name
    #
    # def set_name(self, name):
    #    self.__name = name

    # Magic getter/setter
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

# p1 = Person("Mark", 20, 6)
# print(p1.public_prop)
#
# print(p1.name)
# # print(p1.get_name())   # Works (not after adding @ to define a magic getter)
# p1.name = "Anna"
# print(p1.name)
# # print(p1.get_name())
# # print(Person.get_name(p1))
#
#
# # p1.name = "Jake"
# # print(p1.name)
# # print(p1.get_name())
#
# print(p1.height)
# p1.height = 7
# print(p1.height)
#
#
#
# print("Script is ending")
#
# # print(p1.name)     # Does not work because the attribute is private
# # print(p1.age)      # Does not work because the attribute is private
# # print(p1.height)   # Does not work because the attribute is private
# # print(p1.__name)      # Does not work