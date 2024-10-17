import json
from src.Vacancy import Vacancy
from abc import ABC, abstractmethod

class Saver(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: Vacancy):
        pass

class JSONSaver(Saver):
    def __init__(self, file_name='vacancy.json'):
        self.__file_name = file_name
        with open(f'{self.__file_name}.json', 'w', encoding='utf-8') as f:
            json.dump([], f, ensure_ascii=False, indent=4)



    def add_vacancy(self, vacancy: Vacancy):
        vac = {'name': vacancy.name,
               'salary': vacancy.salary,
               'url': vacancy.url,
               'id': vacancy.id}

        with open(f'{self.__file_name}.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        if not isinstance(data, list):
            data = list(data)
        if vac not in data:
            data.append(vac)


        with open(f'{self.__file_name}.json', 'w', encoding='utf-8') as f:
            json.dump(list(data), f, ensure_ascii=False, indent=4)

    def delete_vacancy(self, vacancy: Vacancy):
        with open(f'{self.__file_name}.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        if not isinstance(data, list):
            data = list(data)
        for i in data:
            if vacancy.id == i.get("id"):
                data.remove(i)

        with open(f'{self.__file_name}.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
