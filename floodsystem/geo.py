# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from .stationdata import stations

def stations_by_distance(stations, p):
    station_name = []
    station_coord = []
    station_town = []
    for each_station in stations:
        list_lines = str(each_station).splitlines()  # splitting data in a list, each component = each line of station info
        counter=0 # initialising counter to count each line of station info
        for each_line in list_lines:
            counter += 1 # adding one to counter for each line of station info e.g. 1 is Station name, 2 is id etc...
            items = each_line.split(': ') # splitting each line into a list (e.g. [Station name, Bourton Dickler])
            items = items [1::2] # removing list descriptor e.g. removing Station name
            if counter == 1: # if the item is the first in the list it is a station name
                items = str(items)[6:-2] # getting rid of white spaces etc
                station_name.append(items)
            if counter == 4: # if the item is the fourth in the list it is the station coordinates
                items = str(items)[5:-2] # getting rid of white spaces etc
                station_coord.append(items)
            if counter == 5: # if the item is the fifth in the list it is the town name
                items = str(items)[11:-2] # getting rid of white spaces etc
                station_town.append(items)

    # turning coordinates from string in list into tuples with float numbers
    station_coord2 = []
    for i in station_coord:
        i = i.strip('()')
        i = i.split(',')
        c = tuple(float(x) for x in i)
        station_coord2.append(c)

    # using haversine function to find distance (using unit = km)
    distances_list = []
    for coord in station_coord2:
        distance = haversine(p, coord, unit='km')
        distances_list.append(distance)
    station_coord_tuples = list(zip(station_name, station_town, distances_list))  # making a list of tuples for each name and coord
    sorted = sorted_by_key(station_coord_tuples, 2, reverse=False) # the distance is the thrid entry in the tuple, therefore, the number entried should be '2' instead of '1'
    return sorted  # sorting tuple according to distance