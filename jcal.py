import typer
import pandas as pd
import json

app = typer.Typer()

@app.command("yearLookup")
def jCalConvert (year):
    f = open('calObj.json')
    j = json.load(f)

    # Handle edge cases
    if type(year) != int:
        try:
            int(year)
        except:
            return "Please enter valid year"
    
    elif year > 10000:
        return "Please specify a valid year"
    
    elif year < 645:
        return "Data only available from 645 CE"
    
    # Logic for search by year. Returns full object
    for key, obj in j.items():
        start_year = float(obj['Start'].split('.')[0])
        end_year = float(obj['End'].split('.')[0])

        if start_year <= year <= end_year:
            return obj
    
