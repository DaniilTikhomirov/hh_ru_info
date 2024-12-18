import os.path
from pathlib import Path

import requests

from src.config_log import setting_log

logger = setting_log("utils")


def write_xml_from_web(url: str, name: str) -> None:
    """
    записывает xml файл с сайта
    :param url:ссылка на сайт
    :param name:имя файла
    :return: None
    """
    req = requests.get(url)
    logger.info("get request")
    with open(os.path.join(Path(__file__).resolve().parents[1], "data", f"{name}.xml"), "wb") as file:
        logger.info("write xml file")
        file.write(req.content)
