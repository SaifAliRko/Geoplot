# folium
# a library to create several types of leaflet maps and also provide fucntions of zooming and click around



# folium.Map()
# This class method will always be the first thing that you execute when working with Folium.
# The purpose of this function is to generate the default map object that will be rendered by your notebook,
# and the object that we will be building on top of for our visualizations.


# folium.FeatureGroup()
# you can put things in it and handle them as a single layer.

# add_child
# Add object child to the first map and store it for the second. ie kind of that drop offs on google maps for example


# 1st part
import numpy as np
import pandas as pd
import folium as fo  # see line 1
%matplotlib inline

# 2nd part

map = fo.Map()  # see line 6

map           # to see world map

a = fo.FeatureGroup( name = 'My Map')

a.add_child(fo.Marker(location = [27.1750,78.0422] , popup = 'hey' , icon = fo.Icon(color = 'blue')))
# Marker is for kind of drop off ie location and the popup message and the color of icon

map.add_child(a)           # adding child with the featured group layer on to the earth maps


# 3rd part

for lat, lon in ([34,53],[24,-50],[90,-68]):

    a.add_child(fo.Marker(location = [lat,lon] , popup = 'hey' , icon = fo.Icon(color = 'red')))

map.add_child(a)           # display the newly added markups or drop offs

# 4th part

volcano = pd.read_csv('volcano.csv') # read the file using pandas

lat_vo = list(volcano['Latitude'])      # will store the whole column of langitude in volcanos lists
lon_vo = list(volcano['Longitude'])
name_vo = list(volcano['Name'])

vol = fo.FeatureGroup( name = 'My Map')

for lat,lon,name in zip(lat_vo,lon_vo,name_vo):

    vol.add_child(fo.Marker(location = [lat,lon] , popup = name , icon = fo.Icon(color = 'red')))   # updating every value by looping

map.add_child(vol)

# 5th part

vol .add_child(fo.GeoJson(data = (open('world.json' , 'r' , encoding = 'utf-8-sig').read())))
# fo.GeoJson for loading json file , opening and reading json file using encoding and read method updated by Folium
# for json file you didnt need to update location adding marker popup name or icon

map.add_child(vol)         # it will just add polygen ie borders blue borders to the specific area which is under observation


# 6th part

popu = pd.read_csv('us cities pop.csv')

popu.head()     # will display 5 rows and 4 columns

lat_po = list(popu['lat'])
lon_po = list(popu['lon'])
name_po = list(popu['name'])
pop_po = list(popu['pop'])

po = fo.FeatureGroup(name = 'My Map')

def mar(popu):                   # function that will be used below
    if (popu>35000):
        return 'red'
    elif (popu>10000 and popu<=35000):
        return 'blue'
    else:
        return 'green'

for lat, lon, name , pop in zip(lat_po , lon_po , name_po , pop_po):  # when the files get very huge its better to use zip
    po.add_child(fo.Marker(location = [lat,lon] , popup = [pop , name] , icon = fo.Icon(color = mar(pop)))) # a fucntion defined as mar above

map.add_child(po)
