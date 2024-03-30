from typing import Optional

import typer
import json

from rich import print
from jcc.console import console

from jcc import __app_name__, __version__
from jcc.utils.utils import yearChecker, eraSearch, calConvert, isKanji

app = typer.Typer()
f = open("./data/calObj.json")
j = json.load(f)


def _versionCallback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__}, v{__version__}")
        raise typer.Exit()


@app.command(
    "era",
    help="Convert Japanese era name to romaji. Verbose mode provides full details of that era",
)
def eraLookup(
    year: str,
    verbose: Optional[bool] = typer.Option(
        None, "--v", "-v", help="Give all era details"
    ),
):
    console.print(eraSearch(j, year, verbose))


@app.command(
    "convert",
    help="Convert Western calendar year to Japanese Imperial calendar, or Japanese Imperial calendar year to Western year",
)
def convert(year):

    yearChecker(year)
    console.print(calConvert(j, year))


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        "--v",
        help="Show application version and exit.",
        callback=_versionCallback,
        is_eager=True,
    )
) -> None:
    return
