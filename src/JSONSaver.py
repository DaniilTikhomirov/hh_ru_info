import json
from abc import ABC, abstractmethod

from src.Vacancy import Vacancy


class Saver(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy) -> None:
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: Vacancy) -> None:
        pass

    @abstractmethod
    def clear(self) -> None:
        pass


class JSONSaver(Saver):
    """класс для сохранения вакансий в json"""

    def __init__(self, file_name: str = "vacancy.json") -> None:
        self.__file_name = file_name
        with open(f"{self.__file_name}.json", "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False, indent=4)

    def clear(self) -> None:
        """очитска json"""
        with open(f"{self.__file_name}.json", "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False, indent=4)

    def add_vacancy(self, vacancy: Vacancy) -> None:
        """обавление вакансии в json"""
        vac = {"name": vacancy.name, "salary": vacancy.salary, "url": vacancy.url, "id": vacancy.id}

        with open(f"{self.__file_name}.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, list):
            data = list(data)
        if vac not in data:
            data.append(vac)

        with open(f"{self.__file_name}.json", "w", encoding="utf-8") as f:
            json.dump(list(data), f, ensure_ascii=False, indent=4)

    def delete_vacancy(self, vacancy: Vacancy) -> None:
        """удаление вакансии с json"""
        with open(f"{self.__file_name}.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, list):
            data = list(data)
        for i in data:
            if vacancy.id == i.get("id"):
                data.remove(i)

        with open(f"{self.__file_name}.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
