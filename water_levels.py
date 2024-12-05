import pandas as pd
import geopandas as gpd
from datetime import datetime
import requests

def get_usgs_water_levels(site_id = "10010000", start_date = "2024-12-01"):
   
    # get water level data from USGS Slatair Boat Harbor site 10010000

    base_url = "https://waterservices.usgs.gov/nwis/iv/"
    params = {
        "format": "json",
        "sites": site_id,
        "startDT": start_date,
        "parameterCd": "62614" # parameter code for groundwater level above NAVD 1988 in meters
    }

    response = requests.get(base_url, params=params)
    data = response.json()
    data = data['value']['timeSeries'][0]['values'][0]['value'] # setting data to relevant data within json (water level value)
#reminder to fix quotes later
    water_df = pd.DataFrame(data)
    water_df['dateTime'] = pd.to_datetime(water_df['dateTime'])
    water_df['value'] = pd.to_numeric(water_df['value'])

    print(water_df)


if __name__ == "__main__": # for testing
    get_usgs_water_levels()