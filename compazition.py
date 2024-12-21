#Продемонстрируйте полиморфизм

class Animal():
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Уф!...Ну что-за дичь пошла бестолковая!Я пол дня за ней бегал, чтобы сфотографировать.")

class Cat(Animal):
    def make_sound(self):
        print("Неправильно ты, дядя Федор бутерброд ешь.")

class Cow(Animal):
    def make_sound(self):
        print("Если бы я поумнее была, я б не молоко давала, а воду газированную!")


animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.make_sound()