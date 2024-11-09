import pytest

from src.Vacancy import Vacancy


@pytest.fixture
def data() -> Vacancy:
    return Vacancy("Senior Java Engineer", 120000, "https://hh.ru/vacancy/108465690", "108465690")


def test_magic(data: Vacancy) -> None:
    vacancy = Vacancy("Senior Java Engineer", 12000, "https://hh.ru/vacancy/108465690", "108465690")
    assert data > vacancy


def test_build_vacancies() -> None:
    data = {
        "alternate_url": "https://hh.ru/vacancy/108635504",
        "id": "108635504",
        "name": "Бэкенд-разработчик в Яндекс (Python/Java/Go/C++/Kotlin)",
        "salary": None,
    }
    vacancy = Vacancy.build_vacancies(data)
    assert vacancy.id == data["id"] and vacancy.salary == 0.0
