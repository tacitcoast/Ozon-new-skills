# Создайте класс-наследник Person, который будет хранить данные абстрактного преподавателя. Назовите его Professor.
# У класса Professor должны быть все параметры класса Person, плюс дополнительный параметр - название курса, который читает преподаватель.
# Кроме того, у класса Professor должен быть метод test_students, который получает на вход список студентов и для
# каждого студента устанавливает случайную оценку от 0 до 10 с помощью метода set_test_score класса Student.
# Переопределите метод __str__ таким образом, чтобы информация о преподавателе выводилась в формате “Преподаватель: Семен Семенов читает курс ООП”
# Создайте список из нескольких студентов. Создайте объект-преподавателя.
# Сделайте так, чтобы преподаватель провел для студентов 2 теста. После каждого из тестов распечатайте состояния студентов.

import random


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


class Professor(Person):

    def __init__(self, name, surname, course_name):
        super().__init__(name, surname)
        self.course_name = course_name

    def test_students(self, list_students):
        for i in list_students:
            i.set_test_score(random.randint(0, 10))

    def __str__(self):
        return 'Преподаватель: {} {}, читает курс {}'.format(self.name, self.surname, self.course_name)


student_one = Student('Любовь', 'Любченка', 'МГУ 2308', [])
student_two = Student('Мария', 'Маркова', 'МГУ 2309', [])

students = [student_one, student_two]
professor = Professor('Виталий', 'Анатольевич', 'Кинематические уравнения движения материальной точки')

print(professor)

professor.test_students(students)

print(student_one)
print(student_two)

professor.test_students(students)

print(student_one)
print(student_two)
