#Tak 2B
#function that returns a list of tuples, holds
# (i) a station (object) at which the latest relative water level is over tol and 
# (ii) the relative water level at the station.
#sorted by the relative level in descending order.

from .station import MonitoringStation
from .utils import sorted_by_key

def stations_level_over_threshold(stations, tol):
    station_rlevel = []
    station_name = []
    for station in stations:
        if MonitoringStation.relative_water_level(station) is not None:
            if float(MonitoringStation.relative_water_level(station)) > float(tol):
                station_name.append(station.name)
                station_rlevel.append(MonitoringStation.relative_water_level(station))
    name_rlevel_tuples = list(zip(station_name,station_rlevel))
    return sorted_by_key(name_rlevel_tuples,1,reverse=True)


#Task 2C
#a list of the N stations (objects) at which the water level, 
# relative to the typical range, is highest.
def stations_highest_rel_level(stations, N):
    station_rlevel = []
    station_name = []
    for station in stations:
        if MonitoringStation.relative_water_level(station) == None:
            pass
        else:
            station_name.append(station.name)
            station_rlevel.append(MonitoringStation.relative_water_level(station))
    name_rlevel_tuples = list(zip(station_name,station_rlevel))
    sorted_list = sorted_by_key(name_rlevel_tuples,1,reverse=True)
    n = int(N)
    return sorted_list[ : n ]
