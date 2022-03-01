#Test print list of relative ranges
from floodsystem.stationdata import build_station_list, update_water_levels
stations = build_station_list()
update_water_levels(stations)

from floodsystem.station import MonitoringStation
station_rlevel = []
for station in stations:
    if MonitoringStation.relative_water_level(station) == None:
        pass
    else:
        station_rlevel.append(MonitoringStation.relative_water_level(station))
'''print(station_rlevel)'''

#First time run encountered negative numbers.
#Test print to see if the current level is negative
current_level = []
for station in stations:
    current_level.append(station.latest_level)
'''print(current_level)'''
#Yes, there are negative current levels



