from unittest.mock import patch

import pytest

from src.HH import HeadHunterAPI


@pytest.fixture
def data() -> list:
    return [
        {"salary": {"currency": "RUR", "from": 80000, "gross": False, "to": 90000}, "url": "url"},
        {"salary": {"currency": "RUR", "from": 70000, "gross": False, "to": 60000}, "url": "url"},
        {"salary": {"currency": "RUR", "from": 90000, "gross": False, "to": 190000}, "url": "url"},
    ]


def test_load_vacancies() -> None:
    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = {
            "items": [{"id": 0, "name": "developer", "salary": {"from": 100000, "to": 200000}}]
        }
        mock_get.return_value.status_code = 200
        hh = HeadHunterAPI()
        hh.load_vacancies("developer", 1)
        assert hh.vacancies == [{"id": 0, "name": "developer", "salary": {"from": 100000, "to": 200000}}]


def test_get_top_vacancies(data: list) -> None:
    with patch("src.HH.get_currencies") as mock_currency:
        mock_currency.return_value = {"RUB": "1"}
        hh = HeadHunterAPI()
        hh.vacancies = data
        top = hh.get_top_vacancies(3)
        assert top == [
            {"salary": {"currency": "RUR", "from": 90000, "gross": False, "to": 190000}, "url": "url"},
            {"salary": {"currency": "RUR", "from": 80000, "gross": False, "to": 90000}, "url": "url"},
            {"salary": {"currency": "RUR", "from": 70000, "gross": False, "to": 60000}, "url": "url"},
        ]


def test_get_vacancies_for_descriptions_keyword(data: list) -> None:
    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = {"description": "python dev"}
        hh = HeadHunterAPI()
        hh.vacancies = data
        vac = hh.get_vacancies_for_descriptions_keyword("py")
        assert vac == [
            {"salary": {"currency": "RUR", "from": 80000, "gross": False, "to": 90000}, "url": "url"},
            {"salary": {"currency": "RUR", "from": 70000, "gross": False, "to": 60000}, "url": "url"},
            {"salary": {"currency": "RUR", "from": 90000, "gross": False, "to": 190000}, "url": "url"},
        ]
