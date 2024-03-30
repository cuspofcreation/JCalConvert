import typer
import json
import logging

from typing import Optional
from jcc.console import console
from jcc import __app_name__, __version__
from jcc.utils.utils import eraSearch, calConvert


logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
app = typer.Typer()

try:
    f = open("./data/calObj.json")
except:
    raise FileNotFoundError("Unable to open calObj.json")

j = json.load(f)


def _versionCallback(value: bool) -> None:
    if value:
        logging.info(f"{__app_name__}, v{__version__}")
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
    logging.info(f"Performing era lookup for year: {year}")
    console.print(eraSearch(j, year, verbose))


@app.command(
    "convert",
    help="Convert Western calendar year to Japanese Imperial calendar, or Japanese Imperial calendar year to Western year",
)
def convert(year):
    logging.info(f"Performing calendar conversion for year: {year}")
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
