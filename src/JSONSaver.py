import json
from src.Vacancy import Vacancy


class JSONSaver:
    def __init__(self, file_name):
        self.file_name = file_name
        with open(f'{self.file_name}.json', 'w', encoding='utf-8') as f:
            json.dump([], f, ensure_ascii=False, indent=4)

    def add_vacancy(self, vacancy: Vacancy):
        vac = {'name': vacancy.name,
               'salary': vacancy.salary,
               'url': vacancy.url,
               'id': vacancy.id}

        with open(f'{self.file_name}.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        if not isinstance(data, list):
            data = list(data)
        data.append(vac)

        with open(f'{self.file_name}.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def delete_vacancy(self, vacancy: Vacancy):
        with open(f'{self.file_name}.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        if not isinstance(data, list):
            data = list(data)
        for i in data:
            if vacancy.id == i.get("id"):
                data.remove(i)

        with open(f'{self.file_name}.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
