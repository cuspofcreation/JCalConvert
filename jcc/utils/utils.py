import datetime
import json
import typer
import re


def yearChecker(year):

    # if type(year) == int:
    if year.isdigit():
        year = int(year)

        # Handle edge cases: Prevent out-of-bounds dates
        if year > datetime.date.today().year:
            raise typer.BadParameter("Please specify a valid year")

        elif year < 645:
            raise typer.BadParameter("Data only available from 645 CE")


def isKanji(inputString):

    # Checks whether inputString is only kanji characters
    if re.fullmatch(r"^[\u4e00-\u9fff]+$", inputString):
        return True
    else:
        return False


# Splits Japanese calendar inputs into an era string and a year string
def split_string_int(inputString: str):

    if type(inputString) != str:
        return "Please specify a valid year"

    match = re.match(r"([^\d]+)(\d+)", inputString)

    if not match:
        match = re.match(r"(\D+)(\d+)", inputString)

    if match:
        return {"era": match.group(1), "year": int(int(match.group(2)))}

    else:
        return "Please specify a valid year"


# Retrieves the corresponding era object for a given Western or Japanese Imperial calendar year.
def eraSearch(json, year):

    if year.isdigit():
        year = int(year)
        for key, obj in json.items():
            start_year = float(obj["Start"].split(".")[0])
            end_year = float(obj["End"].split(".")[0])

            if start_year <= int(year) <= end_year:
                return obj

    else:

        if not (re.search(r"\d", year)):

            for key, obj in json.items():
                if year == obj["Japanese"] or year == obj["Era_no_diacritics"]:
                    return obj

        else:

            input_split = split_string_int(year)

            for key, obj in json.items():

                if (
                    input_split["era"] == obj["Japanese"]
                    or input_split["era"] == obj["Era_no_diacritics"]
                ):
                    return obj


# Take in a date string in the form either, e.g., 平成21 or Heisei 21
def calConvert(json, year):

    if year.isdigit():
        for key, obj in json.items():
            start_year = float(obj["Start"].split(".")[0])
            end_year = float(obj["End"].split(".")[0])

            if start_year <= int(year) <= end_year:
                era_name = obj["Era name"]
                start_year = float(obj["Start"])
                era_year = int(year) - int(start_year) + 1
                return f"{era_name} {era_year}"

    else:
        input_split = split_string_int(year)
        resultMatrix = []

        for key, obj in json.items():
            if (
                input_split["era"] == obj["Japanese"]
                or input_split["era"] == obj["Era_no_diacritics"]
            ):
                searchResult = []
                start_year = float(obj["Start"])

                searchResult.append(obj["Japanese"])
                searchResult.append(obj["Era name"])
                searchResult.append(int(start_year) + input_split["year"] - 1)
                resultMatrix.append(searchResult)

    return resultMatrix
