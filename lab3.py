import re
import Shelf
from task2 import *

if __name__ == "__main__":
    # Задание 1 Вариант 7
    q = Shelf.Book(1, 'Заметки на полях', "Вадим", "Аверсэв", '20/02/2002', 213, 221, "7Б")
    q1 = Shelf.Book(2, 'Лилия в янтаре', "Никита", "Аверсэв", '17/02/2005', 553, 541, "2Б")
    q2 = Shelf.Book(3, 'Дорогами', "Андрей", "Аверсэв", '13/02/2001', 213, 761, "5Б")
    q3 = Shelf.Book(4, 'Картины доисторической жизни человека', "Вадим", "Аверсэв", '06/02/2011', 333, 121, "7Б")
    library = Shelf.Shelf()
    library.add_list(q)
    library.add_list(q1)
    library.add_list(q2)
    library.add_list(q3)
    name = "Вадим"
    year = 2002
    y = library.get_list_of_author(name)
    y2 = library.after_year(year)
    print("Книги автора {0}: ".format(name), end=" ")
    for _ in y:
        print(_.name, end=". ")
    print()
    print('список книг, выпущенных после {0} года:'.format(year), end=" ")
    for _ in y2:
        print(_.name, end=". ")

    # Задание 2 Вариант 11
    engine = Engine('Бензиновый')
    railwayCarriage = RailwayCarriage(100)
    car = Car(3232, "Volvo", "Седан", "Задний", engine)
    train = Train(32232, "Volvo", 250, "Минск - Гомель", engine, railwayCarriage)
    Express = Express(32232, "Volvo", 250, "Минск - Гомель", engine, railwayCarriage, 200)
    print("\n\nЗадание2\n")
    print(engine)
    print(railwayCarriage)
    print(car)
    print(train)
    print(Express)




