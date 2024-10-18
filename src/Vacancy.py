class Vacancy:
    """класс вакансии"""

    __slots__ = ["__name", "__salary", "__url", "__id"]

    def __init__(self, name: str, salary: float, url: str, id_: str) -> None:
        self.__name = name
        self.__salary = self.__salary_not_none(salary)
        self.__url = url
        self.__id = id_

    @staticmethod
    def __salary_not_none(salary: float | None) -> float:
        """валидатор зарплаты"""
        if salary is None:
            return 0.0
        return salary

    def __lt__(self, other: "Vacancy") -> bool:
        return self.salary < other.salary

    def __gt__(self, other: "Vacancy") -> bool:
        return self.salary > other.salary

    @classmethod
    def build_vacancies(cls, data: dict) -> "Vacancy":
        """преврощает словарь в вакансию"""
        salary = data.get("salary")
        if salary is not None:
            if salary.get("to") is None:
                salary = salary.get("from")
            else:
                salary = salary.get("to")

        return cls(
            data.get("name", "notFound"), salary, data.get("alternate_url", "notFound"), data.get("id", "notFound")
        )

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
