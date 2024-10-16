import json

from src.HH import HeadHunterAPI
from src.JSONSaver import JSONSaver
from src.Vacancy import Vacancy

# Создание экземпляра класса для работы с API сайтов с вакансиями

# Получение вакансий с hh.ru в формате JSON
# Преобразование набора данных из JSON в список объектов

# Пример работы контструктора класса с одной вакансией
# Сохранение информации о вакансиях в файл


def full_data(tag: str):
    hh_api = HeadHunterAPI()
    hh_api.load_vacancies("Python developer")
    hh_vacancies = hh_api.vacancies
    json_saver = JSONSaver("info")
    for element in hh_vacancies:
        vacancy = Vacancy.build_vacancies(element)
        json_saver.add_vacancy(vacancy)





