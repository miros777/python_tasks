'''
Створити клас Rectangle:
-він має приймати дві сторони x,y
-описати поведінку на арифметични методи:
  + сумма площин двох екземплярів ксласу
  - різниця площин двох екземплярів ксласу
  == площин на рівність
  != площин на не рівність
  >, < меньше більше
  при виклику метода len() підраховувати сумму сторін
'''
from string import printable
from typing import Self


class Rectangle:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def len(self):
        return (self.y + self.x) * 2

    def sum_tow_obj(self, other: Self):
        return self.len() + other.len()

    def min_2(self, other: Self):
        return (self.y + self.x) * 2 - (other.x + other.y) * 2

    def __eq__(self, other: Self):
        if other is None or not isinstance(other, Rectangle):
            return False
        return self.len() == other.len()

    def __lt__(self, other: Self):
        if other is None or not isinstance(other, Rectangle):
            return False
        return self.len() < other.len()

    def __gt__(self, other: Self):
        if other is None or not isinstance(other, Rectangle):
            return False
        return self.len() > other.len()

    def __str__(self):
        return self.__dict__


# rec_1 = Rectangle(15,20)
# rec_2 = Rectangle(10,20)
# print(rec_1.len())
# print(rec_2.len())
#
#
# print(rec_1 == rec_2)
# print(rec_1 > rec_2)
# print(rec_1 < rec_2)


'''
  ###############################################################################

створити класс Human (name, age)
створити два класси Prince и Cinderella які наслідуються від Human:
у попелюшки мае бути ім'я, вік, розмір нонги
у принца має бути ім'я, вік, та розмір знайденого черевичка, а також метод котрий буде приймати список попелюшок, та шукати ту саму

в класі попелюшки має бути count який буде зберігати кількість створених екземплярів классу
також має бути метод классу який буде виводити це значення
'''


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Cinderella(Human):
    __count = 0

    def __init__(self, name, age, size_foot):
        super().__init__(name, age)
        self.size_foot = size_foot
        Cinderella.__count += 1

    def __str__(self):
        return str(self.__dict__)

    @classmethod
    def get_count(cls):
        return cls.__count


class Prince(Human):
    def __init__(self, name, age, size_shoe):
        super().__init__(name, age)
        self.size_shoe = size_shoe

    def find_cinderella(self, cinder_list: list[Cinderella]):
        for cinderella in cinder_list:
            if cinderella.size_foot == self.size_shoe:
                print(cinderella)
                return


cind_list: list[Cinderella] = [
    Cinderella('Olha', 25, 32),
    Cinderella('Kira', 18, 36),
    Cinderella('Albina', 30, 16),
    Cinderella('Maria', 25, 15)
]
prince = Prince('Max', 15, 32)
prince.find_cinderella(cind_list)

Cinderella.get_count()
'''

###############################################################################

1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable
3) Створити клас Main в якому буде:
- змінна класу printable_list яка буде зберігати книжки та журнали
- метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають є класом Book або Magazine инакше ігрнорувати додавання
- метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
- метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу
'''
from abc import ABC, abstractmethod


class Printable(ABC):
    @abstractmethod
    def print(self):
        pass


class Book(Printable):
    def __init__(self, name):
        self.name = name

    def print(self):
        print(self.name)


class Magazine(Printable):
    def __init__(self, name):
        self.name = name

    def print(self):
        print(self.name)


class Main:
    __printable_list: list[Printable] = []

    @classmethod
    def add(cls, item:Book|Magazine):
        if isinstance(item, Magazine) or isinstance(item, Book):
            cls.__printable_list.append(item)

    @classmethod
    def show_all_magazines(cls):
        for magazine_one in cls.__printable_list:
            if isinstance(magazine_one, Magazine):
                magazine_one.print()

    @classmethod
    def show_all_books(cls):
        for book in cls.__printable_list:
            if isinstance(book, Book):
                book.print()

Main.add(Magazine('magazine1'))
Main.add(Magazine('magazine4'))
Main.add(Book('book1'))
Main.add(Book('book2'))
Main.add(Magazine('magazine3'))
Main.add(Book('book3'))
Main.add(Magazine('magazine2'))
Main.add(Book('book4'))
Main.add('ddddddddddddddd')

Main.show_all_magazines()
print('********************************************')
Main.show_all_books()
