from jcc.utils.utils import yearChecker
import datetime
import pytest

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


def test_prehistoric_year():
    with pytest.raises(Exception) as e_info:
        year = "600"
        yearChecker(year)
    assert str(e_info.value) == "Data only available from 645 CE"
