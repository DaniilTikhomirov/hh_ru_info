from typing import Any
import json


class Vacancy:

    def __init__(self, name: str, salary: float, url: str, id_: str) -> None:
        self.__name = name
        if salary is None:
            salary = 0.0
        self.__salary = salary
        self.__url = url
        self.__id = id_

    @staticmethod
    def cast_to_object_list(vacancies: Any):
        return json.load(vacancies)

    @classmethod
    def build_vacancies(cls, data: dict) -> 'Vacancy':
        salary = data.get('salary')
        if salary is not None:
            if salary.get('to') is None:
                salary = salary.get('from')
            else:
                salary = salary.get('to')



        return cls(data.get("alternate_url", "notFound"), salary,
                   data.get('alternate_url', "notFound"),
                   data.get('id', "notFound"))

    @property
    def name(self) -> str:
        return self.__name

    @property
    def salary(self) -> float:
        return self.__salary

    @property
    def url(self) -> str:
        return self.__url

    @property
    def id(self) -> str:
        return self.__id
