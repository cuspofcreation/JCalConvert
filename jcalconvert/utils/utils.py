import datetime
import json
import typer

f = open('./data/calObj.json')
json = json.load(f)

# Handles year inputs 
def yearChecker(year: int):

    # Handle edge cases
        if type(year) != int:
            try:
                int(year)
            except:
                return "Please specify a valid year"
        
        elif year > datetime.date.today().year:
            raise typer.BadParameter("Please specify a valid year")
        
        elif year < 645:
            raise typer.BadParameter("Data only available from 645 CE")

# Retrieves the corresponding era object for a given Gregorian calendar year.
def eraFinder(json, year: int, converter: bool):
    for key, obj in json.items():
        start_year = float(obj['Start'].split('.')[0])
        end_year = float(obj['End'].split('.')[0])

        if start_year <= year <= end_year:
            if (not(converter)):
                return obj
            else:
                era_name = obj['Era name']
                start_year = float(obj['Start'])
                era_year = int(year - start_year + 2)
                return(f'{era_name} {era_year}')
                
        
# 
# take in a date string in the form either, e.g., 平成21 or Heisei 21
