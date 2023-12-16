from typing import Optional

import typer
import json
import datetime

from jcalconvert import __app_name__, __version__

app = typer.Typer()
f = open('./data/calObj.json')
j = json.load(f)

def _versionCallback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__}, v{__version__}")
        raise typer.Exit()

@app.command("era")
def eraLookup (year: int, verbose: Optional[bool] = typer.Option(None, "--v", help="Give all era details"), convert: Optional[bool] = typer.Option(None, "--c", help="Convert Gregorian calendar date to Japanese Imperial calendar date")):

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
            if verbose:
                print(obj)
            else:
                print(obj['Era name'])
            return

@app.command("convert")
def convert(year: int):

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
                era_name = obj['Era name']
                era_year = int(year - start_year + 1)
                print(f'{era_name} {era_year}')
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
