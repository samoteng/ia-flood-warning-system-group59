#demonstration programme
#prints the name of each station at which the current relative level is over 0.8, 
#with the relative level alongside the name

from floodsystem.stationdata import build_station_list, update_water_levels
stations = build_station_list()
update_water_levels(stations)

from floodsystem.flood import stations_level_over_threshold
list = stations_level_over_threshold(stations,0.8)
for i in list:
    print('Stations overthreshold are:',i)
