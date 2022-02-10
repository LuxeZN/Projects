# et2100 Fall 21/22 - Project 3 Task 1 Template File
#
# This file contains a skeleton code for project 3 task 1
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
# 11182021 - Version 1.2 - Changed to run for Project 3 - Zach Naymik

#import modules needed to run program
import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

#identify file name we want to run
filename = 'earthquakes-19940117.json'

#open and extract the data from the json file
with open(filename) as f:
    all_eq_data = json.load(f)
    print(len(all_eq_data))


#extracts the longitudes and latitudes from the json data
#also puts the data in their respective lists
lons = []
lats = []
for features in all_eq_data['features']:
    lons.append(features['geometry']['coordinates'][0])
    lats.append(features['geometry']['coordinates'][1])

#extracts the magnitudes from the json data and puts it into its list
mags = []
for features in all_eq_data['features']:
    mags.append(features['properties']['mag'])
    

#creates and plots the data on the scattergeo plot
data = [{
    'type' : 'scattergeo',
    'lon' : lons,
    'lat' : lats,
    'marker' : {'size':[10*mag for mag in mags],
                'color': mags,
                'colorscale': 'Viridis',
                'reversescale': True,
                'colorbar':{'title':'Magnitude'},

                },
    }]

#creates the name of the plot and creates the html file the graph is saved on
my_layout = Layout(title = 'Global Earthquakes')
fig = {'data':data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
