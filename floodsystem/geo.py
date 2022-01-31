# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

#Task 1B
from hashlib import new
from .utils import sorted_by_key  
from haversine import haversine, Unit

def stations_by_distance(stations, p):
    station_name = []
    station_town = []
    station_coord = []   
    for station in stations:
        station_name.append(station.name) #making a list of station names 
        station_town.append(station.town) #making a list of station towns
        station_coord.append(station.coord) #making a list of station coordinates as string
    
    # using haversine function to find distance, unit = km
    distances_list = []
    for coord in station_coord:
        distance = haversine(p, coord, unit='km')
        distances_list.append(distance)
    
    station_coord_tuples = list(zip(station_name, station_town, distances_list))  # making a list of tuples of (name, town, distance)
    sorted = sorted_by_key(station_coord_tuples, 2, reverse=False) 
    return sorted  # sorting tuple according to distance



#Task 1C
def stations_within_radius(stations, centre, r):
    list = stations_by_distance(stations, centre) #create list of stations with distances to compare with r
    new_list = []
    for unit in list:
        if unit[2] < float(r): #each unit consists of tuple (name, town, distance), distance is the 2nd element
            new_list.append(unit[0])
    new_list.sort()
    return(new_list)