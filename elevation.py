import requests
import pandas as pd
import time


# script for returning elevation from lat, long, based on open elevation data
# which in turn is based on SRTM
def get_elevation(lat, long):
    query = ('https://api.open-elevation.com/api/v1/lookup'
             f'?locations={lat},{long}')
    r = requests.get(query).json()  # json object, various ways you can extract value
    # one approach is to use pandas json functionality:
    elevation = pd.io.json.json_normalize(r, 'results')['elevation'].values[0]
    return elevation


tic = time.perf_counter()
for x in range(10):
    for y in range(10):
        print(get_elevation(x, y))

toc = time.perf_counter()
print(f"Done in {toc - tic:0.4f} seconds")
