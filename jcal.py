import pandas as pd
import json

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
    
    
    print(j)