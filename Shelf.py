import types

import re
import Shelf
class Book:

    def __init__(self, id=-1, name='', author='', publishing='', year=-1, str_number=-1, price=-1, type=''):
        if self.re_id(id):
            self.id = id
        else:
            self.id = -1
            print("Введены неверные данные. Информация не записана")

        if self.re_name(name):
            self.name = name
        else:
            self.name = ''
            print("Введены неверные данные. Информация не записана")

        if self.re_author(author):
            self.author = author
        else:
            self.author = ''
            print("Введены неверные данные. Информация не записана")

        if self.re_publishing(publishing):
            self.publishing = publishing
        else:
            self.publishing = ''
            print("Введены неверные данные. Информация не записана")

        if self.re_year(year):
            self.year = year
        else:
            self.year = -1
            print("Введены неверные данные. Информация не записана")

        if self.re_str_number(str_number):
            self.str_number = str_number
        else:
            self.str_number = -1
            print("Введены неверные данные. Информация не записана")

        if self.re_price(price):
            self.price = price
        else:
            self.price = -1
            print("Введены неверные данные. Информация не записана")

        if self.re_type(type):
            self.type = type
        else:
            self.type = ''
            print("Введены неверные данные. Информация не записана")

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_author(self):
        return self.author

    def get_publishing(self):
        return self.publishing

    def get_year(self):
        return self.year

    def get_str_number(self):
        return self.str_number

    def get_price(self):
        return self.price

    def get_type(self):
        return self.type

    def set_id(self, id):
        if self.re_id():
            self.id = id
        else:
            print("Введены неверные данные. Информация не записана")

    def set_name(self, name):
        if self.re_name():
            self.name = name
        else:
            print("Введены неверные данные. Информация не записана")

    def set_author(self, author):
        if self.re_author():
            self.author = author
        else:
            print("Введены неверные данные. Информация не записана")

    def set_publishing(self, publishing):
        if self.re_publishing():
            self.publishing = publishing
        else:
            print("Введены неверные данные. Информация не записана")

    def set_year(self):
        if self.re_id():
            self.id = id
        else:
            print("Введены неверные данные. Информация не записана")

    def set_str_number(self, str_number):
        if self.re_str_number():
            self.str_number = str_number
        else:
            print("Введены неверные данные. Информация не записана")

    def set_price(self, price):
        if self.re_price():
            self.price = price
        else:
            print("Введены неверные данные. Информация не записана")

    def set_type(self, type):
        if self.re_type():
            self.type = type
        else:
            print("Введены неверные данные. Информация не записана")

    @staticmethod
    def re_id(id):
        #  id содержит последовательность цифр длиной не более 5
        test = re.fullmatch(r'[0-9]{1,5}', str(id))
        return test

    @staticmethod
    def re_name(name):
        # name содержит строку нижнего и верхнего регистров и пробелы
        test = re.fullmatch(r'[а-яА-Я ]+', str(name))
        return test

    @staticmethod
    def re_author(author):
        # author содержит строку нижнего и верхнего регистров и пробелы
        test = re.fullmatch(r'[а-яА-Я ]+', str(author))
        return test

    @staticmethod
    def re_publishing(publishing):
        # publishing содержит строку нижнего и верхнего регистров, пробелы и цифры
        test = re.fullmatch(r'[а-яА-Я0-9 ]+', str(publishing))
        return test

    @staticmethod
    def re_year(year):
        # year содержит дату в формате dd/mm/yyyy
        test = re.fullmatch(r'\d\d/\d\d/\d{4}', str(year))
        return test

    @staticmethod
    def re_str_number(str_number):
        # str_number содержит строку нижнего и верхнего регистров и пробелы(не более 10000)
        test = re.fullmatch(r'[0-9]{1,5}', str(str_number))
        return test

    @staticmethod
    def re_price(price):
        # price содержит цифры
        test = re.fullmatch(r'[0-9]+', str(price))
        return test

    @staticmethod
    def re_type(type):
        # type содержит строку нижнего и верхнего регистров и пробелы
        test = re.fullmatch(r'[а-яА-Я0-9 ]+', str(type))
        return test

    def __setattr__(self, attr, value):
        if attr == 'id' or attr == 'name' or attr == 'author' or attr == 'publishing' or \
                attr == 'year' or attr == 'str_number' or attr == 'price' or attr == 'type':
            self.__dict__[attr] = value
        else:
            raise AttributeError(attr + ' not allowed')


class Shelf:
    def __init__(self):
        self.list = []

    def add_list(self, val):
        # добавляем только книги
        if isinstance(val, Book):
            self.list.append(val)

    def get_list_of_author(self, author):
        lst = []
        for _ in self.list:
            if _.author == author:
                lst.append(_)
        return lst

    def after_year(self, year):
        lst = []
        for _ in self.list:
            spam = str(_.year)[-4:]
            if int(spam) > year:
                lst.append(_)
        return lst
