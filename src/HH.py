from abc import ABC, abstractmethod
from decimal import Decimal
from typing import Any

import requests

from src.curency import get_currencies


class Parser(ABC):

    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def load_vacancies(self, keyword: str) -> None:
        pass

    @abstractmethod
    def get_top_vacancies(self, n: int) -> list:
        pass

    @abstractmethod
    def get_vacancies_for_descriptions_keyword(self, keyword: str, vacancy: list | None = None) -> list:
        pass


class HeadHunterAPI(Parser):
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом, который вам необходимо реализовать
    """

    def __init__(self) -> None:
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params: Any = {"text": "", "page": 0, "per_page": 100, "search_fields": ["skills", "title"]}
        self.__vacancies: list[dict] = []
        self.__ids: list[int] = []

    def __contains(self, vacancy: list) -> None:
        """добавление в лист только тех вакансий которые не повторялись"""
        for vac2 in vacancy:
            if vac2["id"] not in self.__ids:
                self.__ids.append(vac2["id"])
                self.__vacancies.append(vac2)

    def __connect_api(self) -> None:
        """подключение к апи"""
        response = requests.get(self.__url, headers=self.__headers, params=self.__params)
        print(response.status_code)
        if response.status_code == 200:
            vacancies = response.json()["items"]
            self.__contains(vacancies)

    def load_vacancies(self, keyword: str, n: int = 5) -> None:
        """загрузка вакансий в список"""
        self.__params["text"] = keyword
        while self.__params.get("page") != n:
            self.__connect_api()
            self.__params["page"] += 1

    @staticmethod
    def __config_key(x: dict, dict_currency: dict) -> Any:
        """переназночение не правильных ключей"""
        salary = x["salary"]
        if salary is None:
            return Decimal("0")
        currency = salary.get("to", 0)
        if currency is None:
            currency = salary.get("from", 0)
            if currency is None:
                currency = 0
        code = salary.get("currency", "RUB")
        if code == "RUR":
            code = "RUB"
        elif code == "BYR":
            code = "BRL"

        return Decimal(dict_currency[code]) * currency

    def get_top_vacancies(self, n: int) -> list:
        """
        нахождение топ вакансий
        :param n: сколько вакасий надо вернуть
        :return: список вакансий
        """
        if n >= len(self.__vacancies):
            n = len(self.__vacancies) - 1
            print("your n > length vacancies")
        print(self.__vacancies)
        if n < 1:
            return []
        dict_currency = get_currencies(
            [
                "AUD",
                "AZN",
                "GBP",
                "AMD",
                "BYN",
                "BGN",
                "BRL",
                "HUF",
                "VND",
                "HKD",
                "GEL",
                "DKK",
                "AED",
                "USD",
                "EUR",
                "EGP",
                "INR",
                "IDR",
                "KZT",
                "CAD",
                "QAR",
                "KGS",
                "CNY",
                "MDL",
                "NZD",
                "NOK",
                "PLN",
                "RON",
                "XDR",
                "SGD",
                "TJS",
                "THB",
                "TRY",
                "TMT",
                "UZS",
                "UAH",
                "CZK",
                "SEK",
                "CHF",
                "RSD",
                "ZAR",
                "KRW",
                "JPY",
                "RUB",
            ]
        )
        sort_vacancies = sorted(self.__vacancies, key=lambda x: self.__config_key(x, dict_currency), reverse=True)
        return sort_vacancies[: n + 1]

    def get_vacancies_for_descriptions_keyword(self, keyword: str, vacancy: list | None = None) -> list:
        """находит вакансии по ключевому слову в описании"""
        if vacancy is None:
            vacancy = self.__vacancies
        new_list: list = []
        for vac in vacancy:
            url = vac["url"]
            response = requests.get(url)
            if keyword.lower() in response.json().get("description", "").lower():
                new_list.append(vac)
        return new_list

    @property
    def url(self) -> str:
        return self.__url

    @property
    def vacancies(self) -> list:
        return self.__vacancies

    @vacancies.setter
    def vacancies(self, data: list) -> None:
        self.__vacancies = data
