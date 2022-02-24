
<<<<<<< HEAD
=======
#Test if function returns tuple

 
 
 #Test the distance is less than 10km
from floodsystem.geo import stations_by_distance
>>>>>>> 67edb9397f50e856454d690ae4d9f008faf23728
from floodsystem.stationdata import build_station_list
from haversine import haversine, Unit
stations = build_station_list()

#Test fo iC: the distance is less than 10km
from floodsystem.geo import stations_by_distance
def check_stations_within_radius(stations, centre, r):
    list = stations_by_distance(stations, centre) #create list of stations with distances to compare with r
    new_list = []
    for unit in list:
        if unit[2] < float(r): #each unit consists of tuple (name, town, distance), distance is the 2nd element
            new_list.append(unit[2])
    return(new_list)
list_2 = check_stations_within_radius(stations, (52.2053, 0.1218), 10)
for i in list_2:
    assert float(i) < 10, 'Should only list stations within 10 km'
print(list_2)



<<<<<<< HEAD
#Test for 1F: list of inconsistent ranges
=======
from floodsystem.stationdata import build_station_list
>>>>>>> 67edb9397f50e856454d690ae4d9f008faf23728
from floodsystem.station import test_inconsistent_typical_range_stations
list_3 = test_inconsistent_typical_range_stations(stations)
print(list_3)
