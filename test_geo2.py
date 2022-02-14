#Test if function returns tuple
print(type(list[0]))
 
 
 #Test the distance is less than 10km
from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list
stations = build_station_list()

def check_stations_within_radius(stations, centre, r):
    list = stations_by_distance(stations, centre) #create list of stations with distances to compare with r
    new_list = []
    for unit in list:
        if unit[2] < float(r): #each unit consists of tuple (name, town, distance), distance is the 2nd element
            new_list.append(unit[2])
    return(new_list)
list_2 = check_stations_within_radius(stations, (52.2053, 0.1218), 10)
print(list_2)

#Test print list of inconsisitent data


from floodsystem.stationdata import build_station_list
from floodsystem.station import test_inconsistent_typical_range_stations
stations = build_station_list()
list_2 = test_inconsistent_typical_range_stations(stations)
print(list_2)
