# et2100 Fall 21/22 20/21 - Project 3 Task 2 Template File
#
# This file contains a skeleton code for project 3 task 2.
# It currently can not run since few variables are missing.
# Add those variables first to make it run a see what happens.
# After you add your code you should modify this header
# to reflect your work.
# Before you submit your project also rename this file.
# Also add yourself as the author of the program
# (do not remove the current author).
# Add also version history

# Authors: Dusan Sormaz and Zach Naymik

# History:
# 04012021 - Version 1.0 - Original file
# 11092021 - Version 1.1 - Changed semester to fall 21/22
# 11192021 - Version 1.2 - Changed to make file work

#import modules needed to run code
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
import json
import math
import requests
from datetime import datetime
from datetime import date

# read data from the API file
json_header = {
        'Accept':'application+json'
        }
url = "https://corona.lmao.ninja/v2/countries"

res = requests.get(url, headers=json_header)
country_json = []
print (f'\nStatus is {res.status_code}')
if res.status_code == 200:
    country_json = res.json()
    print(country_json)
    print(country_json[0].keys())

# inspect the data

# print sample of the data in python to verify it

#initialize data lists

# define necessary data as lists

# retrieve the data for each country
longs = []
lats = []
country_names = []
covid_cases = []
for i in country_json:
    longs.append(i['countryInfo']['long'])
    lats.append(i['countryInfo']['lat'])
    country_names.append(i['country'])
    covid_cases.append(i['cases'])

#verify the data 
print(lats[:10])
print(longs[:10])
print(country_names[:10])
print(covid_cases[:10])

#make strings for the actual date
now = datetime.now()
print(now)
just_date = date.today()
print(just_date)

#define a plot

data = [{
    'type' : 'scattergeo',
    'lon' : longs,
    'lat' : lats,
    'text' : country_names,
    'marker' : {'size':[math.sqrt(c)/25 for c in covid_cases],
                'color': covid_cases,
                'colorscale': 'Delta',
                'reversescale': True,
                'colorbar':{'title':'Magnitude'},
                },
    }]

#modify the title and file name to include the date variable

my_layout = Layout(title = 'Total COVID-19 Cases by country at {}'.format(now))

fig = {'data':data, 'layout': my_layout}
offline.plot(fig, filename='world_cases_{}.html'.format(just_date))
