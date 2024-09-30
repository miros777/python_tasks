"""
1) Є ось такий файл... ваша задача записати в новий файл тільки email'ли з доменом gmail.com (Хеш то що з ліва записувати не потрібно)
"""
import json
from operator import attrgetter
from os import write
from typing import TypedDict

try:
    with open('emails.txt', 'r+') as file,  open('new_file.txt', 'w') as new_file:
        for line in file:
            if line.find('@gmail.com') != -1:
                res = line.split()[-1] # розділяємо по пробілах і беремо останній
                new_file.write(f'{res}\n')
except Exception as e:
    print(e)

"""
2) Створити записну книжку покупок:
- у покупки повинна бути id, назва і ціна
- всі покупки зберігаємо в файлі
з функціоналу:
 * вивід всіх покупок
 * має бути змога додавати покупку в книгу
* має бути змога шукати по будь якому полю покупку
* має бути змога показати найдорожчу покупку
* має бути можливість видаляти покупку по id
(ну і меню на це все)
"""
# class Purchases:
#     def __init__(self, file_name: str):
#         self.__file_name = file_name
#         self.__purchases_list = []
#         self.__read_file()
#         self.__id = self.__gen_id()
#
#     def __show_all(self):
#         for purchase in self.__purchases_list:
#             print(f'{purchase["id"]}) {purchase["name"]} - {purchase["price"]}')
#
#     def __add(self):
#         name = input('Enter name: ')
#
#         while True:
#             try:
#                 price = float(input('Enter price: '))
#                 break
#             except (Exception,):
#                 pass
#
#         new_purchase = {'id':next(self.__id), 'name':name, 'price':price}
#         self.__purchases_list.append(new_purchase)
#         self.__write_file()
#
#     def __find_by(self):
#         value = input('Enter value: ')
#
#         for purchase in self.__purchases_list:
#             if value in [str(item) for item in purchase.values()]:
#                 print(purchase)
#
#     def __most_expensive(self):
#         print(max(self.__purchases_list, key=lambda x: x.get('price')))
#
#     def __delete_by_id(self):
#         self.__show_all()
#
#         while True:
#             try:
#                 _id = int(input('Enter id: '))
#                 break
#             except (Exception,):
#                 pass
#
#         index = next((i for i, v in enumerate(self.__purchases_list) if v['id'] == _id), None)
#
#         if index:
#             del self.__purchases_list[index]
#             self.__write_file()
#             return
#
#         print('Error')
#
#     def menu(self):
#         while True:
#             print('*' * 50, end='\n\n')
#             print('1) Show all')
#             print('2) Create')
#             print('3) Find by')
#             print('4) Most expensive')
#             print('5) Delete by id')
#             print('9) Exit')
#
#             choice = input('make your choice: ')
#             print('*'*50, end='\n\n')
#             match choice:
#                 case '1':
#                     self.__show_all()
#                 case '2':
#                     self.__add()
#                 case '3':
#                     self.__find_by()
#                 case '4':
#                     self.__most_expensive()
#                 case '5':
#                     self.__delete_by_id()
#                 case '9':
#                     return
#
#     def __write_file(self):
#         try:
#             with open(self.__file_name, 'w') as file:
#                 json.dump(self.__purchases_list, file)
#         except Exception as err:
#             print(err)
#
#     def __read_file(self):
#         try:
#             with open(self.__file_name) as file:
#                 self.__purchases_list = json.load(file)
#         except (Exception,):
#             self.__write_file()
#
#     def __gen_id(self):
#         _id = self.__purchases_list[-1]['id']+1 if self.__purchases_list else 1
#         while True:
#             yield _id
#             _id += 1
#
#
#
# purchases = Purchases('notebook.txt')
# # purchases.menu()
# purchases.add()
# # purchases.show_all()
# # purchases.find_by()
# # purchases.most_expensive()
# # purchases.delete_by_id()
#
# pass

class Book_Buy:
    # __all_skeshual:list = []

    def __init__(self, all_book_by:str ):
        self.__file_by = all_book_by
        self.__all_book_list = []
        self.__id = self.__gener_id()
        self.__read_file()

    def menu(self):
        while True:
            print('*' * 50, end='\n\n')
            print('1) Show all')
            print('2) Create')
            print('3) Find by')
            print('4) Most expensive')
            print('5) Delete by id')
            print('9) Exit')

            choice = input('make your choice: ')
            print('*' * 50, end='\n\n')
            match choice:
                case '1':
                    self.__show_all()
                case '2':
                    self.__add()
                case '3':
                    self.__find_by()
                case '4':
                    self.__most_expensive()
                case '5':
                    self.__delete_by_id()
                case '9':
                    return

    def __add(self):
        name = input('Enter name: ')

        while True:
            try:
                price = float(input('Enter price: '))
                break
            except (Exception,):
                pass

        new_purchase = {'id': next(self.__id), 'name': name, 'price': price}
        self.__all_book_list.append(new_purchase)
        self.__write_file()

    def __gener_id(self):
        _id = self.__all_book_list[-1]['id']+1 if self.__all_book_list else 1
        while True:
            yield _id
            _id += 1

    def __write_file(self):
        try:
            with open(self.__file_by, 'w') as file:
                json.dump(self.__all_book_list, file)
        except Exception as e:
            print(e)

    def max_price(self):
        max_p = max(self.__all_book_list, key=attrgetter('price'))
        print(max_p.price)

    def __read_file(self):
        try:
            with open(self.__file_by, 'r') as file:
                self.__all_book_list = json.load(file)
        except Exception as e:
            print(e)

    def __show_all(self):
        for purchase in self.__all_book_list:
            print(f'{purchase["id"]}) {purchase["name"]} - {purchase["price"]}')

    def __find_by(self):
        value = input('Enter value: ')

        for purchase in self.__purchases_list:
            if value in [str(item) for item in purchase.values()]:
                print(purchase)

    def __most_expensive(self):
        print(max(self.__purchases_list, key=lambda x: x.get('price')))

    def __delete_by_id(self):
        self.__show_all()

        while True:
            try:
                _id = int(input('Enter id: '))
                break
            except (Exception,):
                pass

        index = next((i for i, v in enumerate(self.__purchases_list) if v['id'] == _id), None)

        if index:
            del self.__purchases_list[index]
            self.__write_file()
            return

        print('Error')

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self)

# one_book:Book_Buy = Book_Buy('notebook.txt')
# one_book.menu()
# one_book.add()
# one_book.show_all()
# one_book.find_by()
# one_book.most_expensive()
# one_book.delete_by_id()
"""
*********Кому буде замало ось завдання з співбесіди
Є ось такий список data
потрібно брати по черзі с кожного списку id і класти в список res, якщо таке значення вже є в результуючому списку то брати наступне з того ж підсписку
"""
data = [
    [
        {"id": 1110, "field": {}},
        {"id": 1111, "field": {}},
        {"id": 1112, "field": {}},
        {"id": 1113, "field": {}},
        {"id": 1114, "field": {}},
        {"id": 1115, "field": {}},
    ],
    [
        {"id": 1110, "field": {}},
        {"id": 1120, "field": {}},
        {"id": 1122, "field": {}},
        {"id": 1123, "field": {}},
        {"id": 1124, "field": {}},
        {"id": 1125, "field": {}},

    ],
    [
        {"id": 1130, "field": {}},
        {"id": 1131, "field": {}},
        {"id": 1122, "field": {}},
        {"id": 1132, "field": {}},
        {"id": 1133, "field": {}},

    ]
]


def cut(arr):
    res = []
    gens = [(i['id'] for i in item if i['id'] not in res) for item in arr]
    while gens:
        gen = gens.pop(0)
        try:
            res.append(next(gen))
            gens.append(gen)
        except StopIteration:
            pass
    return res


print(cut(data))

