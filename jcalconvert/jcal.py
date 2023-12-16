import pandas as pd
import json

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
    
