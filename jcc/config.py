"""This module creates config and confirms database is present /w associated error-handling"""
# jcalconvert/config.py

import configparser
from pathlib import Path

import typer

from jcc import (
    DB_READ_ERROR, DIR_ERROR, FILE_ERROR, SUCCESS, __app_name__
)

CONFIG_DIR_PATH = Path(typer.get_app_dir(__app_name__))
CONFIG_FILE_PATH = CONFIG_DIR_PATH / "config.ini"

# Initialise application
def init_app(db_path: str) -> int:
    """Init app"""
    config_code = _init_config_file()
    if config_code != SUCCESS:
        return config_code
    db_code = _check_database(db_path)
    if db_code != SUCCESS:
        return db_code
    return SUCCESS

# Generate config file
def _init_config_file() -> int:
    try:
        CONFIG_DIR_PATH.mkdir(exist_ok=True)
    except OSError:
        return DIR_ERROR
    try:
        CONFIG_FILE_PATH.touch(exist_ok=True)
    except OSError:
        return FILE_ERROR
    return SUCCESS

# Check DB is present
def _check_database(db_path: str) -> int:
    config_parser = configparser.ConfigParser()
    config_parser["General"] = {"database": db_path}
    try:
        with CONFIG_FILE_PATH.open("r") as file:
            config_parser.read(file)
    except OSError:
        return DB_READ_ERROR
    return SUCCESS