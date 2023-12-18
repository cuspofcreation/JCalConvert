from typing import Optional

import typer
import json

from jcalconvert import __app_name__, __version__
from jcalconvert.utils.utils import yearChecker, eraFinder

app = typer.Typer()
f = open('./data/calObj.json')
j = json.load(f)

def _versionCallback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__}, v{__version__}")
        raise typer.Exit()

@app.command("era", help="Lookup corresponding era name for Western (Gregorian) calendar year")
def eraLookup (
    year: int, 
    verbose: Optional[bool] = typer.Option(None, "--v", help="Give all era details"), 
    ):

    yearChecker(year)
    
    res = eraFinder(j, year)
    
    if (verbose):
         print(res)
    else: print(res['Era name'])

@app.command("convert", help="Convert Western (Gregorian) calendar year to Japanese Imperial Calendar")
def convert(
    year: int,
    j2g: Optional[bool] = typer.Option(None, "--j2g", "j2g", help="Convert Japanese Imperial calendar date to Gregorian"),
    g2j: Optional[bool] = typer.Option(None, "--g2j", "g2j", help="Convert Western (Gregorian) calendar year to corresponding Japanese Imperial calendar dates")
    ):

    # Handle edge cases
    yearChecker(year)
    
    #Convert Gregorian year input to Japanese Imperial calendar
    print(eraFinder(j, year, converter=True))

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
