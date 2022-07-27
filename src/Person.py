class Person():

    classAttr = "成员变量"

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.__gender = gender

    def get_name(self):
        return self.age
    def testMethod():
        print(" classs method")

    def get_gender(self):
        return self.__gender

    @age.setter
    def age(self, age):
        print("aaa " + self)
