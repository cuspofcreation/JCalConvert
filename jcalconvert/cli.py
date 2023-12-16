from typing import Optional

import typer
import json
import datetime

from jcalconvert import __app_name__, __version__

app = typer.Typer()

def _versionCallback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__}, v{__version__}")
        raise typer.Exit()
    

@app.command("era")
def eraLookup (year: int):
    f = open('./data/calObj.json')
    j = json.load(f)

    # Handle edge cases
    if type(year) != int:
        try:
            int(year)
        except:
            return "Please enter valid year"
    
    elif year > datetime.date.today().year:
        print("Please specify a valid year")
        return
    
    elif year < 645:
        print("Data only available from 645 CE")
        return
    
    # Logic for search by year. Returns full object
    for key, obj in j.items():
        start_year = float(obj['Start'].split('.')[0])
        end_year = float(obj['End'].split('.')[0])

        if start_year <= year <= end_year:
            print(obj)
            return

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
