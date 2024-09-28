# 1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
# - перший записує в список нову справу
# - другий повертає всі записи
from itertools import count
from typing import Callable


def notebook() -> tuple[Callable[[str], None], Callable[[], list[str]]]:
    todo_list: list[str] = []

    def add_todo(todo: str) -> None:
        nonlocal todo_list
        todo_list.append(todo)

    def get_all_todo() -> list[str]:
        nonlocal todo_list
        return todo_list.copy()

    return get_all_todo, add_todo


add_n_1 = notebook()
add_n_2 = notebook()
get_all_todo1, add_todo1 = add_n_1
get_all_todo2, add_todo2 = add_n_2

add_todo1('todo_1_1')

add_todo2('todo_5_1')
add_todo2('todo_5_2')

print(get_all_todo1())
print(get_all_todo2())


# 2
def expanded_form(num: int):
    res = []
    st = str(num)
    len_n = len(st) - 1

    for i, ch in enumerate(st):
        if ch != '0':
            res.append(ch + '0' * (len_n - i))

    return ' + '.join(res) + ' = ' + st


print(expanded_form(102055))
print(expanded_form(502577))


# 4) створити декоратор котрий буде підраховувати скільки разів була запущена функція продекорована цим
# декоратором, та буде виводити це значення після виконання функцій

def deco_count(func):
    count = 0

    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print('====')
        print(f'count: {count} \n{func.__name__}')

    return inner


@deco_count
def my_func():
    pass


@deco_count
def my_func2():
    pass


my_func()
my_func2()
my_func2()
my_func2()
my_func()

'''
- є функція:
def pr():
    return 'Hello_boss_!!!'
 написати декоратор до цієї функції, який замінює нижні підчеркування на пробіли і повертає це значення
функцию pr менять не можно
'''


def pr_deco(func):
    def inner(*args, **kwargs):
        list_1 = func()
        res = ''.join([ch.replace('_', ' ') for ch in list_1])
        return res

    return inner


@pr_deco
def pr():
    return 'Hello_boss_!!!'


print(pr())

'''
вивести послідовність Фібоначі, кількість вказана в знінній,
  наприклад: x = 10 -> 1 1 2 3 5 8 13 21 34 55
  (число з послідовності - це сума попередніх двох чисел)
'''

cache = {0: 0, 1: 1}
def fibonacci_of(n):
    if n in cache:  # Base case
        return cache[n]  # Compute and cache the Fibonacci number
    cache[n] = fibonacci_of(n - 1) + fibonacci_of(n - 2)  # Recursive case

    return cache[n]


print([fibonacci_of(n) for n in range(5)])

'''
порахувати кількість парних і непарних цифр числа, 
  наприклад: х = 225688 -> п = 5, н = 1;
         х = 33294 -> п = 2, н = 3
'''

'''
прога, що виводить кількість кожного символа з введеної строки,
  наприклад: 
  st = 'as 23 fdfdg544' #введена строка

  'a' -> 1  #вивело в консолі
  's' -> 1
  ' ' -> 2
  '2' -> 1
  '3' -> 1
  'f' -> 2
  'd' -> 2
  'g' -> 1
  '5' -> 1
  '4' -> 2
'''
st = 'as 23 fdfdg544'
l = []
for i in st:
    l.append(f'{i} -> {st.count(i)}')

list_res = set(l)
for i in list_res:
    print(i)
