from jcc.utils.utils import yearChecker, splitStringInt, eraSearch
import datetime
import pytest
import json


# Test yearChecker
def test_current_year():
    year = str(datetime.date.today().year)
    result = yearChecker(year)
    assert result is None


def test_future_year():
    with pytest.raises(Exception) as e_info:
        year = "2035"
        yearChecker(year)
    assert str(e_info.value) == "Please specify a valid year"


def test_past_year():
    year = "1612"
    result = yearChecker(year)
    assert result is None


def test_year_645():
    year = "645"
    result = yearChecker(year)
    assert result is None


def test_year_before_645():
    with pytest.raises(Exception) as e_info:
        year = "600"
        yearChecker(year)
    assert str(e_info.value) == "Data only available from 645 CE"


# Test splitStringInt
def test_splitStringInt_valid_input_en():
    year = "Heisei 21"
    result = splitStringInt(year)
    assert result == {"era": "Heisei ", "year": 21}


def test_splitStringInt_valid_input_jp():
    year = "平成21"
    result = splitStringInt(year)
    assert result == {"era": "平成", "year": 21}


def test_splitStringInt_invalid_input_onlynums():
    year = "123"
    result = splitStringInt(year)
    assert result == "Please specify a valid year"


def test_splitStringInt_invalid_input_onlychars():
    year = "aBc"
    result = splitStringInt(year)
    assert result == "Please specify a valid year"
