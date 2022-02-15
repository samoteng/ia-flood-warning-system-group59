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
        if MonitoringStation.relative_water_level(station) < float(tol):
            station_name.append(station.name)
            station_rlevel.append(MonitoringStation.relative_water_level(station))
    name_rlevel_tuples = list(zip(station_name,station_rlevel))
    return sorted_by_key(name_rlevel_tuples,1,reverse=True)
