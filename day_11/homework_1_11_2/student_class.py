# Создайте класс-наследник Person, который будет хранить данные абстрактного студента. Назовите его Student.
# У класса Student должны быть все параметры класса Person, плюс два дополнительных параметра:
# - Номер группы
# - Список оценок по тестам
# Также у класса Student должен быть дополнительный метод set_test_score, получающий на вход оценку по тесту и добавляющий ее в список оценок студента.
# Переопределите метод __str__ таким образом, чтобы информация о студенте выводилась в формате “Студент: Иван Иванов, группа ГР-01, оценки [5, 0]”
# Создайте несколько объектов класса Student, распечатайте их параметры с помощью print.


class Person:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return 'Это {} {}'.format(self.name, self.surname)


class Student(Person):

    def __init__(self, name, surname, group_number, list_of_test_scores):
        super().__init__(name, surname)
        self.group_number = group_number
        self.list_of_test_scores = list_of_test_scores

    def set_test_score(self, grades):
        self.list_of_test_scores.append(grades)

    def __str__(self):
        return 'Студент: {} {}, группа {}, оценки {}'.format(self.name, self.surname, self.group_number, self.list_of_test_scores)


student_one = Student('Любовь', 'Любченка', 'МГУ 2308', [])
student_two = Student('Мария', 'Маркова', 'МГУ 2309', [])

student_one.set_test_score(5)
student_two.set_test_score(4)
student_one.set_test_score(4)
student_two.set_test_score(3)

print(student_one)
print(student_two)
