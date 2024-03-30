import datetime
import json
import typer
import re

from rich.table import Table
from jcc.console import console


# Ensures year is not in the future, nor before 645CE
def yearChecker(year):

    # if type(year) == int:
    if year.isdigit():
        year = int(year)

        # Handle edge cases: Prevent out-of-bounds dates
        if year > datetime.date.today().year:
            raise typer.BadParameter("Please specify a valid year")

        elif year < 645:
            raise typer.BadParameter("Data only available from 645 CE")


# Checks whether inputString is only kanji characters
def isKanji(inputString):

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


# Returns a rich table with either the era name or full era details for a given Western or Japanese Imperial calendar year.
def eraSearch(json, year, verbose):

    resultTable = Table(show_header=True, header_style="bold", show_lines=True)

    # Would love a smarter way to do this
    if verbose:
        colNames = [
            "Dates (CE)",
            "Start",
            "End",
            "Era name",
            "Japanese",
            "Period",
            "Events",
        ]

        for name in colNames:
            resultTable.add_column(name)

    else:
        colNames = ["Era", "Romaji"]

        for name in colNames:
            resultTable.add_column(name)

    # Potentially redundant, but retained since its use in verbose mode provides information not covered by calConvert
    if year.isdigit():
        year = int(year)
        console.print("Did you mean to use the convert function?")

        for key, obj in json.items():
            start_year = float(obj["Start"].split(".")[0])
            end_year = float(obj["End"].split(".")[0])

            if start_year <= int(year) <= end_year:

                # Create a new dictionary without the "Era_no_diacritics" key
                filtered_obj = {
                    k: v for k, v in obj.items() if k != "Era_no_diacritics"
                }

                if verbose:
                    # Add row to table
                    resultTable.add_row(
                        *[str(filtered_obj[col]) for col in filtered_obj]
                    )
                else:
                    resultTable.add_row(
                        filtered_obj["Japanese"], filtered_obj["Era name"]
                    )

        return resultTable

    else:
        if not (re.search(r"\d", year)):

            for key, obj in json.items():

                if year == obj["Japanese"] or year == obj["Era_no_diacritics"]:
                    # Create a new dictionary without the "Era_no_diacritics" key
                    filtered_obj = {
                        k: v for k, v in obj.items() if k != "Era_no_diacritics"
                    }

                    if verbose:
                        # Add row(s) to table
                        resultTable.add_row(
                            *[str(filtered_obj[col]) for col in filtered_obj]
                        )

                    else:
                        resultTable.add_row(
                            filtered_obj["Japanese"], filtered_obj["Era name"]
                        )

            return resultTable

        else:

            input_split = split_string_int(year)

            for key, obj in json.items():
                if (
                    input_split["era"] == obj["Japanese"]
                    or input_split["era"] == obj["Era_no_diacritics"]
                ):
                    # Create a new dictionary without the "Era_no_diacritics" key
                    filtered_obj = {
                        k: v for k, v in obj.items() if k != "Era_no_diacritics"
                    }
                    if verbose:
                        # Add row(s) to table
                        resultTable.add_row(
                            *[str(filtered_obj[col]) for col in filtered_obj]
                        )
                    else:
                        resultTable.add_row(
                            filtered_obj["Japanese"], filtered_obj["Era name"]
                        )

        return resultTable


# Take in a date string in the form either, e.g., 平成21 or Heisei 21
def calConvert(json, year):

    resultTable = Table(show_header=True, header_style="bold")
    resultTable.add_column("Era")
    resultTable.add_column("Romaji")

    # Handle Western calendar input
    if year.isdigit():

        resultTable.add_column("Imperial_Year")

        for key, obj in json.items():
            start_year = float(obj["Start"].split(".")[0])
            end_year = float(obj["End"].split(".")[0])

            if start_year <= int(year) <= end_year:
                start_year = float(obj["Start"])

                searchResult = [
                    obj["Japanese"],
                    obj["Era name"],
                    str(int(year) - int(start_year) + 1),
                ]

                resultTable.add_row(*searchResult)
                return resultTable

    # Handle Japanese calendar input
    else:
        input_split = split_string_int(year)
        resultTable.add_column("Gregorian_Year")
        resultMatrix = []

        for key, obj in json.items():
            if (
                input_split["era"] == obj["Japanese"]
                or input_split["era"] == obj["Era_no_diacritics"]
            ):
                start_year = float(obj["Start"])
                end_year = float(obj["End"])
                print(str(end_year))
                convertedYear = int(start_year) + input_split["year"] - 1

                if convertedYear > int(end_year):
                    eraName = obj["Era name"]
                    eraFinalYearImperial = int(end_year) - int(start_year) + 1
                    convertedYear = f"The last year of the {eraName} era was {int(end_year)}, {eraName} {eraFinalYearImperial}"

                # Check whether convertedYear exceeds the final year of the era

                searchResult = [
                    obj["Japanese"],
                    obj["Era name"],
                    str(convertedYear),
                ]

                resultMatrix.append(searchResult)

        for row in resultMatrix:
            resultTable.add_row(*row)

    return resultTable
