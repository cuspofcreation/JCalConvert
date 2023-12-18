import datetime
import json
import typer
import re

# f = open('./data/calObj.json')
# j = json.load(f)

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

# Splits Japanese calendar inputs into an era string and a year string
def split_string_int(input_string: str):

    if type(input_string) != str:
        return ("Please specify a valid year")
    match = re.match(r'([^\d]+)(\d+)', input_string)
    if not match:
        match = re.match(r'(\D+)(\d+)', input_string)
    if match:
        # string_part = match.group(1)
        # int_part = int(match.group(2))
        return { 'era': match.group(1), 'year': int(int(match.group(2))) }
    else:
        return ("Please specify a valid year")
        # return None, None  # Return None if the input format doesn't match

# Retrieves the corresponding era object for a given Gregorian calendar year.
def eraFinder(json, year: int, verbose: bool=False):

    for key, obj in json.items():
        start_year = float(obj['Start'].split('.')[0])
        end_year = float(obj['End'].split('.')[0])

        if start_year <= year <= end_year:
            if (verbose):
                return obj
            else:
                era_name = obj['Era name']
                start_year = float(obj['Start'])
                era_year = int(year - start_year + 2)
                return(f'{era_name} {era_year}')        
        
# take in a date string in the form either, e.g., 平成21 or Heisei 21
def jLookup(json, input_year: str):

    input_split = split_string_int(input_year)

    for key, obj in json.items():

        if input_split['era'] == obj['Japanese'] or obj['Era_no_diacritics']:
            start_year = float(obj['Start'])
            return (int(start_year) + input_split['year'] - 1)

