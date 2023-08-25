# Создайте класс студента.
# Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие
# только букв.
# Названия предметов должны загружаться из файла CSV при создании экземпляра.
# Другие предметы в экземпляре недопустимы.
# Для каждого предмета можно хранить оценки (от 2 до 5) и
# результаты тестов (от 0 до 100).
# Также экземпляр должен сообщать средний балл по тестам для каждого
# предмета и по оценкам всех предметов вместе взятых.
import csv

class Control:

    def __init__(self, is_title, is_digit):
        self.is_title = is_title
        self.is_digit = is_digit

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __set__(self, instance, value):
        if not self.is_title(value):
            raise ValueError(f'Неверный формат записи! ({value})')
        for i in value:
            if self.is_digit(i):
                raise ValueError(f'Неверный формат записи! В ({value}) не должно быть цифр!')
        setattr(instance, self.param_name, value)


class Student:

    first_name = Control(str.istitle, str.isdigit)
    last_name = Control(str.istitle, str.isdigit)
    surname = Control(str.istitle, str.isdigit)

    def __init__(self, first_name, last_name, surname):
        self.first_name = first_name
        self.last_name = last_name
        self.surname = surname
        self._subjects = self.load_subjects()



    def load_subjects(self):
        dict = {}
        with open('subjects.csv', 'r', encoding='utf-8') as f:
            file = csv.reader(f, dialect='excel', delimiter=' ')
            for i in file:
                dict[str(*i)] = {'оценки':[], 'результаты тестов':[]}
            return dict

    def __repr__(self):
        return f'Student({self._first_name}, {self._last_name}, {self._surname})'

    def get_test_res(self, subj):
        res = len(self._subjects[subj]['результаты тестов'])
        if res:
            return sum(i for i in self._subjects[subj]['результаты тестов']) / res
        else: return None


    def set_test_res(self, subj, value):
        if 0 < value < 100:
            self._subjects[subj]['результаты тестов'].append(value)


    def get_grades(self):
        res = sum(len(self._subjects[i]['оценки']) for i in self._subjects)
        if res:
            return sum(j for i in self._subjects for j in self._subjects[i]['оценки']) / res
        else: return None


    def set_grades(self, subj, value):
        if 0 < value < 100:
            self._subjects[subj]['оценки'].append(value)





a = Student('Петров', 'Иван', 'Петрович')
print(a)
print(a._subjects) # вызов в целях демонстрации реализации способа хранения оценок
a.set_grades('математика', 5)
a.set_grades('физика', 4)
a.set_grades('английский', 3)
a.set_grades('программирование', 2)
a.set_grades('программирование', 5)
a.set_test_res('математика', 4)
a.set_test_res('математика', 3)
a.set_test_res('математика', 2)
print(a._subjects) # вызов в целях демонстрации реализации способа хранения оценок
print(a.get_grades())
print(a.get_test_res('математика'))

#____________________________ВЫВОД______________________________
# Student(Петров, Иван, Петрович)
# {'математика': {'оценки': [], 'результаты тестов': []}, 'физика': {'оценки': [], 'результаты тестов': []}, 'английский': {'оценки': [], 'результаты тестов': []}, 'физкультура': {'оценки': [], 'результаты тестов': []}, 'программирование': {'оценки': [], 'результаты тестов': []}}
# {'математика': {'оценки': [5], 'результаты тестов': [4, 3, 2]}, 'физика': {'оценки': [4], 'результаты тестов': []}, 'английский': {'оценки': [3], 'результаты тестов': []}, 'физкультура': {'оценки': [], 'результаты тестов': []}, 'программирование': {'оценки': [2, 5], 'результаты тестов': []}}
# 3.8
# 3.0