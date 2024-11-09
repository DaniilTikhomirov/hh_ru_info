import json

import pytest

from src.JSONSaver import JSONSaver
from src.Vacancy import Vacancy


@pytest.fixture
def data() -> Vacancy:
    return Vacancy("Senior Java Engineer", 120000, "https://hh.ru/vacancy/108465690", "108465690")


def test_add_vacancy(data: Vacancy) -> None:
    vacancy = data
    saver = JSONSaver("test")
    saver.clear()
    saver.add_vacancy(vacancy)
    with open("test.json", "r", encoding="utf8") as f:
        js = json.load(f)
    assert js == [
        {"id": "108465690", "name": "Senior Java Engineer", "salary": 120000, "url": "https://hh.ru/vacancy/108465690"}
    ]


def test_delete_vacancy(data: Vacancy) -> None:
    vacancy = data
    saver = JSONSaver("test")
    saver.clear()
    saver.add_vacancy(vacancy)
    saver.delete_vacancy(vacancy)
    with open("test.json", "r", encoding="utf8") as f:
        js = json.load(f)
    assert js == []


def test_delete_vacancy_null(data: Vacancy) -> None:
    vacancy = data
    saver = JSONSaver("test")
    saver.clear()
    saver.delete_vacancy(vacancy)
    with open("test.json", "r", encoding="utf8") as f:
        js = json.load(f)
    assert js == []


def test_clear(data: Vacancy) -> None:
    vacancy = data
    saver = JSONSaver("test")
    saver.add_vacancy(vacancy)
    saver.clear()
    with open("test.json", "r", encoding="utf8") as f:
        js = json.load(f)
    assert js == []
