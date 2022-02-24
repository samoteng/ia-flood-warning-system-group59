#Demonstration program

from floodsystem.stationdata import build_station_list, update_water_levels
stations = build_station_list()
update_water_levels(stations)

from floodsystem.flood import stations_highest_rel_level
list = stations_highest_rel_level(stations,10)
counter = 1
for i in list:
    print(counter,i)
    counter +=1