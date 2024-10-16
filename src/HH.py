from pprint import pprint

import requests
from abc import ABC, abstractmethod
from src.curency import get_currencies
from decimal import Decimal


class Parser(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def load_vacancies(self, keyword):
        pass

    @abstractmethod
    def get_top_vacancies(self, n: int):
        pass

    @abstractmethod
    def get_vacancies_for_descriptions_keyword(self, keyword, vacancy=None):
        pass


class HeadHunterAPI(Parser):
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом, который вам необходимо реализовать
    """

    def __init__(self):
        self.__url = 'https://api.hh.ru/vacancies'
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.__params = {'text': '', 'page': 0, 'per_page': 100}
        self.__vacancies = []

    def load_vacancies(self, keyword: str):
        self.__params['text'] = keyword
        while self.__params.get('page') != 20:
            response = requests.get(self.__url, headers=self.__headers, params=self.__params)
            vacancies = response.json()['items']
            self.__vacancies.extend(vacancies)
            self.__params['page'] += 1

    @staticmethod
    def config_key(x: dict, dict_currency: dict):
        salary = x["salary"]
        if salary is None:
            return 0
        currency = salary.get('to', 0)
        if currency is None:
            currency = salary.get('from', 0)
            if currency is None:
                currency = 0
        code = salary.get('currency', 'RUB')
        if code == "RUR":
            code = "RUB"
        elif code == "BYR":
            code = "BRL"

        return Decimal(dict_currency[code]) * currency

    def get_top_vacancies(self, n: int):
        if n >= len(self.__vacancies):
            n = len(self.__vacancies) - 1
            print("your n > length vacancies")

        if n < 1:
            return []
        dict_currency = get_currencies(
            ['AUD', 'AZN', 'GBP', 'AMD', 'BYN', 'BGN', 'BRL', 'HUF', 'VND', 'HKD', 'GEL', 'DKK', 'AED', 'USD', 'EUR',
             'EGP',
             'INR', 'IDR', 'KZT', 'CAD', 'QAR', 'KGS', 'CNY', 'MDL', 'NZD', 'NOK', 'PLN', 'RON', 'XDR', 'SGD', 'TJS',
             'THB',
             'TRY', 'TMT', 'UZS', 'UAH', 'CZK', 'SEK', 'CHF', 'RSD', 'ZAR', 'KRW', 'JPY', 'RUB'])
        sort_vacancies = sorted(self.__vacancies, key=lambda x: self.config_key(x, dict_currency), reverse=True)
        new_vacancies = []
        for i in range(n):
            new_vacancies.append(sort_vacancies[n])
        return new_vacancies

    def get_vacancies_for_descriptions_keyword(self, keyword, vacancy=None):
        if vacancy is None:
            vacancy = self.vacancies
        new_list = []
        for vac in vacancy:
            url = vac['url']
            response = requests.get(url)
            if keyword in response.json().get("description", ""):
                print("in")
                new_list.append(vac)
        return new_list

    @property
    def url(self) -> str:
        return self.__url

    @property
    def vacancies(self):
        return self.__vacancies
