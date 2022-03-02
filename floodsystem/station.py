# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None


     #Task 1F: method to check consisitency in typical range
    def typical_range_consistent(self):
        if self.typical_range == None : #stations with no range data
            return False
        if self.typical_range[0] >  self.typical_range[1] : #stations with low range higher than high range, tuple(low, high)
            return False
        else:
            return True
    

    #Task 2B: fraction would be (level-low)/(high-low)
    def relative_water_level(self): 
        if self.typical_range == None : #stations with no range data
            return None
        if self.typical_range[0] >  self.typical_range[1] : #stations with low range higher than high range, tuple(low, high)
            return None
        if self.latest_level == None : #stations with no latest level data
            return None
        else: #stations with suitable data
            level = float(self.latest_level)
            low = float(self.typical_range[0])
            high = float(self.typical_range[1])
            fraction = (level - low)/(high - low)
            return round(fraction,3)


    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d


#Task 1F: returns a list of stations that have inconsistent data    
def inconsistent_typical_range_stations(stations):
    list_inconsistent_stations = []
    for station in stations: #each unit in list
        if MonitoringStation.typical_range_consistent(station) == False :#call function to check consisitency
            list_inconsistent_stations.append(station.name)
    list_inconsistent_stations.sort() #sorting list of names in alphabetical order
    return(list_inconsistent_stations)




