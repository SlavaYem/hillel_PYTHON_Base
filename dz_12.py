# data.json - файл с данными о некоторых математиках прошлого.
# 1. Необходимо написать функцию, которая считает эти данные из файла. Параметр функции - имя файла.
# 2. Написать "функцию сортировки" данных по ФАМИЛИИ в поле "name" (у тех у кого она есть).
# Например для Rene Descartes фамилия это Descartes, у Pierre de Fermat - Fermat и т.д.
# Если фамилии нет, то использовать имя, например Euclid.
# 3. Написать функцию сортировки по количеству слов в поле "text".
# 4. Написать функцию сортировки по дате смерти из поля "years".
# Обратите внимание на сокращение BC. - это означает до н.э.
import json
import re


def read_json_file(filename):
    with open(filename, "r") as file:
        data_1 = json.load(file)
    return data_1


data = read_json_file("data.json")


def sort_surname(item):
    my_name = item["name"]
    my_sort_name = my_name.split()[-1]
    return my_sort_name


sorted_name = sorted(data, key=sort_surname)
print(sorted_name)


def sorted_text_symbols(item):
    my_text = item["text"]
    my_symbols = len(my_text.split())
    return my_symbols


sorted_text = sorted(data, key=sorted_text_symbols)
print(sorted_text)


def sorted_years(item):
    my_years = item["years"]
    template = r".+\s(\d+)\D*$"
    year = re.match(template, my_years).group(1)
    year = -int(year) if ("bc" in my_years.lower()) else int(year)
    return year


years = sorted(data, key=sorted_years)
print(years)
