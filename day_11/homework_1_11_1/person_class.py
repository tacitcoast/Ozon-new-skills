# Создайте класс Person, хранящий базовые данные о каком-нибудь человеке. У класса должно быть два параметра:
# - Фамилия
# - Имя
# И два метода:
# - Конструктор __init__
# - Метод __str__ для вывода объектов на печать.
# Определите метод __str__ таким образом, чтобы при печати объекта выводились имя и фамилия. Например “Иван Иванов”.
# Создайте и распечатайте с помощью print два объекта класса Person с любыми именами и фамилиями.

class Person:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return 'Это {} {}'.format(self.name, self.surname)


person_one = Person('Петр', 'Петров')
person_two = Person('Иван', 'Иванов')

print(person_one)
print(person_two)
