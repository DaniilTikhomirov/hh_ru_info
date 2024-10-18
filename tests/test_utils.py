import os.path
from datetime import datetime
from pathlib import Path
from unittest.mock import patch

from src.utils import write_xml_from_web


def test_write_xml_from_web() -> None:
    with patch("builtins.open") as mock_open:
        with patch("requests.get") as mock_get:
            time_now = datetime.strftime(datetime.now(), "%d/%m/%Y")
            url = f"https://cbr.ru/scripts/XML_daily.asp?date_req={time_now}"
            write_xml_from_web(url, "cbr")
            mock_open.assert_called_once_with(
                os.path.join(Path(__file__).resolve().parents[1], "data", "cbr.xml"), "wb"
            )
            mock_get.assert_called_once_with(f"https://cbr.ru/scripts/XML_daily.asp?date_req={time_now}")
