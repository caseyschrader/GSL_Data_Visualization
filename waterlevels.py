import pandas as pd
import geopandas as gpd
from datetime import datetime
import requests

def get_usgs_water_level(site_id = "10010000", start_date = "2000-01-01"):
   
    # fetch water level data from USGS Slatair Boat Harbor site 10010000

    base_url = "https://waterservices.usgs.gov/nwis/iv/"
    params = {
        "format": "json",
        "sites": site_id,
        "startDT": start_date,
        "parameterCd": "62614" # parameter code for groundwater level above NAVD 1988 in meters
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    print(data)