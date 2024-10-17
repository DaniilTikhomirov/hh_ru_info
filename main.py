import json
from pprint import pprint

from src.HH import HeadHunterAPI
from src.JSONSaver import JSONSaver
from src.Vacancy import Vacancy

# Создание экземпляра класса для работы с API сайтов с вакансиями

# Получение вакансий с hh.ru в формате JSON
# Преобразование набора данных из JSON в список объектов

# Пример работы контструктора класса с одной вакансией
# Сохранение информации о вакансиях в файл


def full_data():
    hh = HeadHunterAPI()
    tag = input("Enter tag: ")
    n = int(input("сколько страниц загрузить? max 20 "))
    if 0 > n or n > 20:
        print("error")
    hh.load_vacancies(tag)
    print("первые пять вакансий")
    pprint(hh.vacancies[:6])
    confirm = input("сохранить в json? Y/N ").lower()
    if confirm == "y":
        file_name = input("введите имя файла")
        saver = JSONSaver(file_name)

        print(f"сколько вакансий сохранить 0-{len(hh.vacancies)}")
        while True:
            num = int(input())
            if 0 < num < len(hh.vacancies):
                break
            else:
                print("не правильный номер попробуйте еще раз")
        print("отсортировать вакансии? Y/N")
        confirm = input().lower()
        if confirm == "y":
            vacancies = hh.get_top_vacancies(num)
        else:
            vacancies = hh.vacancies
        for vacancy in range(num):
            saver.add_vacancy(Vacancy.build_vacancies(vacancies[vacancy]))
        print(f"данные сохранены в {file_name}.json")







if __name__ == "__main__":
    full_data()