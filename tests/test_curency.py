import xml.etree.ElementTree as ET
from unittest.mock import patch

import pytest

from src.curency import get_currencies


@pytest.fixture
def data() -> str:
    return """<?xml version="1.0" encoding="windows-1251"?>
<ValCurs Date="15.05.2024" name="Foreign Currency Market">
    <Valute ID="R01235">
        <NumCode>840</NumCode>
        <CharCode>USD</CharCode>
        <Nominal>1</Nominal>
        <Name>Доллар США</Name>
        <Value>74,3250</Value>
        <VunitRate>74,3250</VunitRate>
    </Valute>
    <Valute ID="R01239">
        <NumCode>978</NumCode>
        <CharCode>EUR</CharCode>
        <Nominal>1</Nominal>
        <Name>Евро</Name>
        <Value>90,1234</Value>
        <VunitRate>90,1234</VunitRate>
    </Valute>
</ValCurs>"""


def test_get_currencies_rub() -> None:
    assert get_currencies(["RUB"]) == {"RUB": "1"}


def test_get_currencies(data: str) -> None:
    with patch("builtins.open") as mock_open:
        with patch("xml.etree.ElementTree.parse") as parse_mock:
            mock_tree = ET.ElementTree(ET.fromstring(data))
            parse_mock.return_value = mock_tree
            mock_file = mock_open.return_value.__enter__.return_value
            mock_file.read.return_value = data
            value = get_currencies(["USD", "EUR"])
            assert value == {"USD": "74.3250", "EUR": "90.1234"}
