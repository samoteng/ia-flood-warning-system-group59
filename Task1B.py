#demonstration program
#list of tuples (station name, town, distance) for the 10 closest and the 10 furthest stations 
#from the Cambridge city centre, (52.2053, 0.1218)

from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list
def run():

    stations = build_station_list()
    list = stations_by_distance(stations,(52.2053, 0.1218))
    print('The closet 10 stations are :', list[:10])
    print('The farthest 10 stations are :', list[-10:])
run()
stations = build_station_list()
list = stations_by_distance(stations,(52.2053, 0.1218))
print('The closet 10 stations are :', list[:10])
print('The farthest 10 stations are :', list[-10:])


#Test if function returns tuple
print(type(list[0]))
 
